# 13 - Selling Printify merch from bettercallzaal.com with Stripe

Researched 2026-10-30, QUICK depth. Goal: the smallest setup that can take money on a shirt.

## Recommendation

**Rung (a), the Printify Pop-Up Store, linked from `/merch`.** It is the Printify and Stripe setup: buyers pay through Stripe at checkout, Printify prints and ships, and earnings reach the bank via Stripe. It needs no code beyond a link, no keys and no monthly fee, and it keeps about $1 more per shirt than the other two.

**This site is not Next.js.** It is static HTML with no build step and no `package.json`, so rung (b) would add this site's first server code, not just a route.

**A Pop-Up Store cannot be embedded.** Measured 2026-10-30 on `zaofestivals.printify.me`: the response header is `content-security-policy: frame-ancestors 'self' https://printify.com https://enterprise.printful.com`, so a browser refuses to show it in an iframe on this site. That is one store, and a seller setting to change it was not looked for. `/merch` links out.

## The three rungs on a $25 shirt

Base cost is Printify's own Pop-Up example ($8.80). Its pricing calculator shows $8.77 for a Unisex Jersey Short Sleeve Tee. Real base cost depends on the product and print provider chosen.

| | (a) Pop-Up Store | (b) Printify API + Stripe Checkout | (c) Shopify + Printify |
|---|---|---|---|
| Sale | $25.00 | $25.00 | $25.00 |
| Printify base | -$8.80 | -$8.80 | -$8.80 |
| Card fee | $0 charged to the seller | -$1.03 (2.9% + 30c) | -$1.03 (2.9% + 30c) |
| **Left per shirt, before shipping and tax** | **$16.20** | **$15.17** | **$15.17** |
| Monthly cost | $0 | $0 | $29 (about 2 shirts a month) |
| Code to build | None | Checkout session, webhook, order creation, failure handling | None |
| Keys | None | Stripe secret, Stripe webhook secret, Printify token | None on this site |
| Who fronts production | Deducted from the sale | Printify charges a card or balance | Printify charges a card or balance |
| Money arrives | 15th of the next month | Stripe's payout schedule | Shopify's payout schedule |
| Support | Printify | Seller | Seller |

Notes on the numbers:

- Stripe's fee also applies to any shipping collected, so (b) and (c) lose slightly more than shown.
- The shipping amount is left out because it depends on provider and address. Stores show it at checkout. Printify's payout formula subtracts production and shipping from total sales, and its example says "$16.20 before shipping", so whether a buyer-paid shipping charge fully covers the cost needs one real order to confirm.
- From Oct 15, 2026 to Jan 17, 2027, every US order carries a flat $0.40 surcharge.
- Shopify's $29 and its 2.9% + 30c card rate are from ZAOOS doc 2508, fetched 2026-09-19, and were not fetched again here.
- Scale check: at $16.20 a shirt, $10,000 takes 618 shirts.

## What rung (a) costs in exchange

- **Slow money.** Earnings pay out on the 15th of the following month. Stripe holds first-ever payouts for 7 days, which can push a first payout back a month.
- **Sales tax is the seller's job.** The Pop-Up seller is the Merchant of Record. Printify does not collect or remit tax on the sale to the buyer. It does charge tax on its own invoice to the seller and withholds that from the sale unless a resale certificate is on file (Wallet, then Taxes). If the margin cannot cover that tax, the order is cancelled and refunded. A search summary of Printify's general Terms described a broader tax-collection clause; that clause was not read directly, and the Pop-Up help page is the more specific source.
- **Printify's return rules apply.** No returns or exchanges. Damaged or defective items get a reprint or refund if reported with a photo within 30 days of delivery.
- **Checkout happens off this site**, on `*.printify.me` or a connected custom domain.
- **No built-in traffic.** Printify says a Pop-Up Store is not a marketplace, so buyers come from Zaal's own links.

Move to (b) only if sales justify it and on-site checkout or faster money becomes worth the upkeep. One thing to settle first: the API docs offer Personal Access Tokens to individual accounts, while the pricing table lists "Custom API integration" under Enterprise only. These may mean different things. This was not resolved.

## State of the existing store

`zaofestivals.printify.me` lists 6 products and **none can be bought today**. Measured 2026-10-30 by fetching all 6 product pages: each shows "This product is coming soon!" and no add-to-cart button. Control: a product page on another Pop-Up store (`official-soa-team-store.printify.me`), fetched the same way, shows "Add to cart" and no coming-soon text. The cause was not established, because the Printify dashboard was not available to this research.

Do not rename that store to repurpose it. Printify says a renamed store's old URL stops working with no redirect, and `merch.zaofestivals.com` points at it.

## Going live on `/merch`

The page shows a closed notice until `merch/store.json` is filled in:

```json
{
  "storeUrl": "https://your-store.printify.me/products",
  "products": [
    {
      "name": "Product name",
      "price": 25,
      "url": "https://your-store.printify.me/product/123/product-name",
      "image": "https://images-api.printify.com/mockup/..."
    }
  ]
}
```

Then remove the `noindex` line from `merch/index.html`, and add `/merch/` to `sitemap.xml` and the home page nav. Prices on this page are typed by hand, so the store's price is the one that counts at checkout.

## Sources

Fetched 2026-10-30.

| Source | Status | Used for |
|---|---|---|
| [Printify Pop-Up Store](https://printify.com/pop-up-store/) | PARTIAL (first 9,000 characters) | $25 on $8.80 example, no fees, payout date, not a marketplace |
| [What is Printify Pop-Up Store?](https://help.printify.com/hc/en-us/articles/12051129478417-What-is-Printify-Pop-Up-Store) | FULL | Stripe checkout, returns, Merchant of Record, store renames |
| [How will my Pop-Up Store earnings be paid out?](https://help.printify.com/hc/en-us/articles/12051908094993-How-will-my-Pop-Up-Store-earnings-be-paid-out) | FULL | Payout formula, 7-day first-payout hold |
| [How does the payment process work?](https://help.printify.com/hc/en-us/articles/4483601124113-How-does-the-payment-process-work) | FULL | Other channels charge the seller's card, Pop-Up exception |
| [What am I responsible for as a Pop-Up Store merchant?](https://help.printify.com/hc/en-us/articles/37390535647889-What-am-I-responsible-for-as-a-Pop-Up-Store-merchant) | PARTIAL (first 2,500 characters) | Merchant of Record, tax |
| [Printify pricing](https://printify.com/pricing/) | PARTIAL (first 9,000 characters) | Plans, $8.77 calculator figure, Custom API integration row |
| [Printify API docs](https://developers.printify.com/) | PARTIAL (overview, auth, order endpoint list) | Tokens, rate limits, order endpoints |
| [Printify shipping rates](https://printify.com/shipping-rates/) | PARTIAL (per-provider rates sit behind further links) | $0.40 surcharge |
| [Stripe pricing](https://stripe.com/pricing) | PARTIAL (first 9,000 characters) | 2.9% + 30c on domestic cards |
| [Stripe Checkout quickstart](https://stripe.com/docs/checkout/quickstart) | PARTIAL (first 5,000 characters; the docs.stripe.com copy returned only its title) | Server endpoint needed |
| [Stripe Checkout overview](https://docs.stripe.com/payments/checkout) | FULL | Hosted Checkout Sessions |
| [Stripe webhooks](https://docs.stripe.com/webhooks) | PARTIAL (first 9,000 characters) | Webhook endpoint needed |
| [Stripe Payment Links](https://docs.stripe.com/payment-links) | FULL | No-code option. It does not create Printify orders by itself |
| printify.com/shipping/ | FAILED (not found) | Replaced by shipping-rates |
| `zaofestivals.printify.me`, its 6 product pages, and the `official-soa-team-store.printify.me` control | Direct fetches | Frame header, product state |
| ZAOOS research doc 2508 | Read in repo | Earlier store comparison, Shopify price |
