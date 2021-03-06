import logging

logger = logging.getLogger('flask_ask')
logger.addHandler(logging.StreamHandler())
if logger.level == logging.NOTSET:
    logger.setLevel(logging.WARN)


from .core import (
    Ask,
    request,
    session,
    version,
    context,
    current_stream,
    convert_errors,
    state,
    slots
)

from .models import (
    question,
    statement,
    audio,
    delegate,
    elicit_slot,
    confirm_slot,
    confirm_intent,
    buy,
    upsell,
    refund,
    setupAmzPay,
    chargeAmzPay
)
