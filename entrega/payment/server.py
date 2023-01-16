# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_51MQB1eBcDq40bal0pJG2uQL65jkkBdwYO9XVc1mKGp315TUZjQQTlcsLuuTeYphfxwApSNaqiHuQcPl9khfNOtbM00Ecl6FSJJ"

stripe.checkout.Session.create(
  line_items=[
    {
      "price_data": {
        "currency": "usd",
        "product_data": {"name": "T-shirt"},
        "unit_amount": 2000,
      },
      "quantity": 1,
    },
  ],
  mode="payment",
  success_url="http://localhost:4242/success.html",
  cancel_url="http://localhost:4242/cancel.html",
)