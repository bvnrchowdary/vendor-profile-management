from django.db.models import Avg, ExpressionWrapper, F, DurationField, Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, HistoricalPerformance
from django.utils import timezone


@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, **kwargs):
    on_time_delivery_rate = 0
    ratings = 0
    response_times = 0
    fulfilment_rate = 0

    completed_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
    on_time_delivered_pos = completed_pos.filter(delivery_date__lte=timezone.now())
    total_completed_pos = completed_pos.count()

    if total_completed_pos > 0:
        on_time_delivery_rate = on_time_delivered_pos.count() / total_completed_pos

    completed_pos_with_ratings = completed_pos.filter(quality_rating__isnull=False)
    if completed_pos_with_ratings:
        ratings = completed_pos_with_ratings.aggregate(Avg('quality_rating'))['quality_rating__avg']

    acknowledged_pos = completed_pos.filter(acknowledgment_date__isnull=False, issue_date__isnull=False)
    if acknowledged_pos:
        total_response_time = acknowledged_pos.annotate(
            response_time=ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=DurationField()
            )
        ).aggregate(Sum('response_time'))['response_time__sum']

        response_times = total_response_time.total_seconds() / 3600 / acknowledged_pos.count()

    all_pos = PurchaseOrder.objects.filter(vendor=instance.vendor)
    successful_fulfilled_pos = all_pos.filter(status='completed', quality_rating__isnull=False)
    total_pos = all_pos.count()
    total_successful_fulfilled_pos = successful_fulfilled_pos.count()

    if total_pos > 0:
        fulfilment_rate = total_successful_fulfilled_pos / total_pos

    HistoricalPerformance.objects.update_or_create(
        vendor=instance.vendor,
        defaults={
            'quality_rating_avg': ratings,
            'on_time_delivery_rate': on_time_delivery_rate,
            'average_response_time': response_times,
            'fulfillment_rate': fulfilment_rate,
            'date': timezone.now(),
        }
    )
