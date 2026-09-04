# Cold / Lead Email Flow - Options for Zaal to Pick

Status: OPTIONS ONLY - nothing configured, nothing sends. Zaal picks, then a
follow-up PR wires the choice. Prepared 2026-08-20 for cowork card 34cbc6f1.

## Context

The site just gained a revenue front door (Build Session offer, PR #37). Leads
currently arrive one way: the Formspree contact form (`mjgajyqe`) emails
zaalp99@gmail.com and dies there - no capture list, no follow-up sequence, no
record in the cowork CRM. "Cold email flow" here means two distinct needs:

1. INBOUND lead capture + follow-up: someone hits the site, raises a hand,
   gets a reply and a next step without falling through the cracks.
2. OUTBOUND cold outreach: Zaal-initiated first-touch emails to prospects
   (Build Session, ZABAL workshops, speaking).

Hard constraints from the repo: pure static site, no build step, no secrets in
the repo. The cowork Supabase already has `contacts` + `contact_log` tables -
a CRM exists; leads should land there.

## Option A (Recommended) - Existing rails, zero new vendors

Capture: keep Formspree, add a dedicated lead form (or fields: budget,
timeline, what-they-want) on the Build Session section.
Book: Cal.com link (already used for ZABAL workshop slots) as the primary CTA -
a booked slot IS the qualified lead.
Record: forward Formspree notification emails into the cowork tracker
(`contacts` + `contact_log`) via the chief-of-staff triage flow; every lead
gets a row and a follow-up task with a due date.
Follow-up: agent drafts replies/sequences as clipboard-ready text; Zaal sends
from his own mail. Nothing automated sends.

- Cost: $0. New vendors: 0. Site change: one form + one CTA link.
- Weakness: follow-up cadence is manual (agent-drafted, Zaal-sent).

## Option B - Buttondown (or similar) capture list + drip

Add an email-capture form posting to Buttondown; leads enter a small drip
sequence (welcome -> case study -> book-a-session). Formspree stays for
general contact.

- Cost: free to ~$9/mo. Real automation for nurture.
- Weakness: new vendor, list overlaps with Paragraph (ZAO newsletter already
  lives there); drip copy is outbound content Zaal must approve per message
  anyway, which erodes the automation win.

## Option C - Resend + Vercel function

Serverless endpoint on the Vercel project handles form posts, writes the lead
to Supabase directly, sends transactional acknowledgment via Resend, and (if
ever approved) sequenced follow-ups from code.

- Cost: free tiers cover the volume. Fully programmable, leads land in the
  CRM with no email-forward hop.
- Weakness: breaks the "pure static, no secrets" ethos of this repo; adds env
  vars + a function to maintain. Overkill until lead volume justifies it.

## Outbound cold email (all options)

Outbound first-touch stays HUMAN-SENT regardless of option: agent researches
prospects and drafts (the /cold-outreach skill exists for this), Zaal reviews
and sends. No bulk sender, no purchased lists - deliverability and reputation
on a personal domain are not worth risking for the volume involved.

## Decision needed from Zaal

1. Pick A, B, or C (or a mix).
2. If A: confirm Cal.com event type to use for Build Session bookings.
3. Approve the lead-form copy before it ships (public-facing).
