"""
THE DISRUPTION DECISION
A Future-of-Banking Strategic Simulation
Executive Development Program (EDP) for Scale IV Executives — Canara Bank

Built for IIM Tiruchirappalli | Department of Finance
Streamlit single-file deployment — one instance per team/group.
"""

import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import io
import re


def md_to_html(text):
    """Convert **bold** / *italic* markdown to real HTML before injecting into a raw
    unsafe_allow_html div — Python-Markdown does not process inline markdown inside raw
    HTML blocks, so without this the literal asterisks render as-is."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text, flags=re.DOTALL)
    text = re.sub(r"(?<!<b>)\*(.+?)\*(?!</b>)", r"<i>\1</i>", text, flags=re.DOTALL)
    return text.replace("\n", "<br>")

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="The Disruption Decision | Future of Banking Simulation",
    page_icon="🏦",
    layout="wide",
)

PRIMARY = "#0B3D91"
ACCENT = "#D4A017"

st.markdown(f"""
<style>
.main-title {{ color:{PRIMARY}; font-size:2.1rem; font-weight:800; margin-bottom:0; }}
.sub-title {{ color:{ACCENT}; font-size:1.05rem; font-weight:600; margin-top:0; }}
.brief-box {{ background-color:#F4F6FB; border-left:6px solid {PRIMARY}; padding:1.1rem 1.3rem;
              border-radius:6px; margin-bottom:1rem; }}
.role-box {{ background-color:#FFF8E8; border-left:6px solid {ACCENT}; padding:1.1rem 1.3rem;
             border-radius:6px; margin-bottom:1rem; }}
.framework-tag {{ display:inline-block; background-color:{PRIMARY}; color:white; font-size:0.72rem;
                   padding:2px 10px; border-radius:12px; margin-left:6px; }}
.phase-header {{ background-color:{PRIMARY}; color:white; padding:0.6rem 1rem; border-radius:6px;
                  font-weight:700; font-size:1.15rem; }}
.budget-note {{ background-color:#FFF4E5; border-left:6px solid #E07B00; padding:0.8rem 1rem;
                 border-radius:6px; font-size:0.92rem; }}
</style>
""", unsafe_allow_html=True)

# ============================================================
# CONFIG DATA
# ============================================================
ROLES = [
    "Chief Strategy & Digital Officer (CSDO)",
    "Chief Risk & Compliance Officer (CRCO)",
    "Head – Technology & GenAI",
    "Head – Retail, MSME & Trade Banking",
    "Head – HR & Talent",
]

PHASES = [
    "0. Briefing",
    "1. Diagnosis & Position",
    "2. Strategy Table (Budget & Negotiation)",
    "3. Board Pitch",
    "4. Debrief Dashboard",
]

SCENARIO_BRIEF = """
**Monday, Q2 FY28. Head Office, Bengaluru.**

The Board has given your leadership team **10 days** to present a 3-year Future-of-Banking strategy,
backed by a ₹300 crore transformation budget. Four pressures have converged just as the deadline
approaches:

1. **Competitive Threat** — *NeoCred*, a GenAI-first fintech-NBFC, has captured **18% of your MSME
   renewal book** in pilot zones over the last two quarters, offering 4-hour GenAI-underwritten
   approvals using UPI/GST transaction data — against your own **7–9 day** turnaround.

2. **AI Governance Red Flag** — Internal audit has found that *Credit-Copilot*, your pilot GenAI
   credit-scoring tool, lacks a documented DPDP-compliant consent trail for part of its training data,
   **and** shows a measurable approval-rate gap across certain geographies — a possible algorithmic-bias
   exposure. The finding lands the same week your strategic bet is due to the Board.

3. **Trade Finance Opportunity/Threat** — Peer banks are piloting blockchain-based electronic Bill of
   Lading (eBL) trade-document digitization, cutting MSME exporters' trade-finance turnaround from
   5 days to same-day. Your Trade Processing Centre still runs largely paper-based LC/BG workflows.

4. **People Issue** — Your senior Trade & MSME manager — 20 years' experience, chairs the zonal MSME
   credit desk, widely respected — is quietly resisting the Credit-Copilot rollout, fearing it will
   devalue judgment-based lending expertise and make their role redundant.

As a leadership team, you must **diagnose, negotiate a strategic bet, and pitch the Board** — without
the governance finding or the people issue becoming afterthoughts to the growth story. Every decision
will be evaluated against the frameworks covered across this program.
"""

ROLE_BRIEFS = {
    "Chief Strategy & Digital Officer (CSDO)": """You are the integrator. You do not own the technical,
risk, or people detail — you depend on your team — but final accountability for the 3-year bet rests
with you. The Board expects **one coherent strategy**, not a growth pitch with the hard parts left out.""",

    "Chief Risk & Compliance Officer (CRCO)": """You own the AI governance and regulatory exposure.
Your obligation to flag the DPDP consent gap and the bias finding exists independent of how much the
strategic timeline is riding on Credit-Copilot. You are the voice that must not be diluted by growth
pressure or convenience.""",

    "Head – Technology & GenAI": """You are the only one in the room who understands the technical
reality of Credit-Copilot and what blockchain/eBL trade digitization actually requires. Your job is to
translate ambition into a credible, sequenced roadmap — not to over-promise speed or kill momentum
with excessive caution.""",

    "Head – Retail, MSME & Trade Banking": """You own the customer and business outcome — the MSME
renewal book NeoCred is eating into, and the Trade Processing Centre's digitization gap. You must
protect revenue and relationships without becoming the voice that resists every change.""",

    "Head – HR & Talent": """You are responsible for the workforce dimension of this transformation,
including a senior, respected manager who is a flight/disengagement risk. Your job is to make the
people plan a first-class part of the strategy, not a footnote after the technology decision.""",
}

# ============================================================
# PHASE 1 — DIAGNOSIS & POSITION (role-specific MCQs)
# ============================================================
PHASE1_QUESTIONS = {
    "Chief Strategy & Digital Officer (CSDO)": [
        {
            "q": "NeoCred is capturing a growing share of your MSME renewal book. What is your first "
                 "move as the integrator?",
            "options": [
                ("Wait for the Technology team to finish evaluating vendors before committing to "
                 "any direction.", 0),
                ("Commission a focused diagnostic (win/loss review + unit economics) and bring Risk, "
                 "Technology, and Business Heads into one strategy sprint before committing capital.", 3),
                ("Approve the largest available GenAI vendor contract immediately to match NeoCred's "
                 "speed.", 1),
                ("Delegate the entire response to the Technology Head alone.", 1),
            ],
            "framework": "Decision-Making & Accountability / Innovative and Digital Mindset",
        },
        {
            "q": "Internal audit's DPDP/bias finding on Credit-Copilot lands the same week the Board "
                 "wants your 3-year bet. What do you do?",
            "options": [
                ("Keep the finding out of the Board pitch to avoid slowing the strategic decision.", 0),
                ("Integrate the governance finding directly into the strategy — no AI scale-up "
                 "commitment without a funded remediation plan — and present both together.", 3),
                ("Pause the entire GenAI programme indefinitely until the finding is fully resolved.", 1),
                ("Let the CRCO handle it separately and keep the Board pitch focused on growth only.", 1),
            ],
            "framework": "Ethics / Decision-Making & Accountability",
        },
    ],
    "Chief Risk & Compliance Officer (CRCO)": [
        {
            "q": "Credit-Copilot has a documented DPDP consent gap and a geography-linked approval-rate "
                 "disparity. What is your obligation?",
            "options": [
                ("Flag it formally with a remediation timeline and insist the model not scale further "
                 "until addressed — regardless of the strategic deadline pressure.", 3),
                ("Raise it informally with the CSDO and let them decide whether to disclose it.", 1),
                ("Note it for the next scheduled compliance review cycle.", 0),
                ("Block the model entirely and refuse any further discussion until next quarter.", 1),
            ],
            "framework": "Compliance & Assurance / Digital Data Protection (DPDP Act, 2023)",
        },
        {
            "q": "How do you assess whether the approval-rate disparity constitutes algorithmic bias "
                 "requiring action under your Ethics obligations?",
            "options": [
                ("It isn't bias unless a customer formally complains.", 0),
                ("Run a structured fairness/disparate-impact check against the geographic variable, "
                 "independent of how useful the model is for speed, before allowing further rollout.", 3),
                ("Assume it is a data-quality issue and leave the model running while it is \"monitored\".", 1),
                ("Rely on the vendor's assurance that their model is \"AI-audited\".", 0),
            ],
            "framework": "Ethics / Artificial Intelligence/Gen-AI in Banking",
        },
    ],
    "Head – Technology & GenAI": [
        {
            "q": "Business wants Credit-Copilot scaled fast to match NeoCred's speed. What is your "
                 "technical stance?",
            "options": [
                ("Scale immediately — speed is what is costing us market share.", 0),
                ("Propose a phased scale-up gated on closing the consent-trail and bias-audit findings "
                 "first, with a committed remediation timeline — not an open-ended pause.", 3),
                ("Recommend abandoning GenAI underwriting entirely given the governance finding.", 1),
                ("Quietly patch the consent documentation without re-running the bias check.", 0),
            ],
            "framework": "Artificial Intelligence/Gen-AI in Banking / Operational Risk Management",
        },
        {
            "q": "For the trade-finance digitization opportunity, how do you advise the Board on "
                 "build-vs-partner?",
            "options": [
                ("Build a proprietary blockchain trade platform from scratch to retain full control.", 1),
                ("Recommend joining an existing bank-backed trade-digitization/eBL consortium rather "
                 "than building from scratch, given timeline and cost realities.", 3),
                ("Recommend waiting for peers to prove the model before doing anything.", 0),
                ("Recommend outsourcing all trade-finance operations to a fintech entirely.", 0),
            ],
            "framework": "Innovative and Digital Mindset / Decision-Making & Accountability",
        },
    ],
    "Head – Retail, MSME & Trade Banking": [
        {
            "q": "MSME customers are leaving for NeoCred's 4-hour turnaround. What is your business "
                 "response?",
            "options": [
                ("Cut interest rates across the board to compete on price alone.", 1),
                ("Target turnaround-time parity for the segments most at risk, while protecting the "
                 "bank's relationship-based underwriting edge for complex/high-value MSME credit the "
                 "fintech can't easily serve.", 3),
                ("Do nothing — loyal customers won't leave.", 0),
                ("Publicly criticise NeoCred's lending practices to customers.", 0),
            ],
            "framework": "Customer Relationship Management / Adaptability",
        },
        {
            "q": "Your Trade Processing Centre still runs largely paper-based LC/BG workflows while "
                 "peers pilot eBL digitization. What do you prioritise?",
            "options": [
                ("Protect the status quo — paper processes are well understood and low-risk.", 0),
                ("Nominate 2–3 top export-corridor branches for a selective digitization pilot, "
                 "building internal capability and a real business case before a full rollout.", 3),
                ("Wait for an RBI/industry mandate before moving.", 1),
                ("Push for immediate full-network digitization without piloting.", 1),
            ],
            "framework": "Innovative and Digital Mindset / Customer Relationship Management",
        },
    ],
    "Head – HR & Talent": [
        {
            "q": "Your senior Trade & MSME manager — 20 years' experience, chairs the zonal MSME credit "
                 "desk — is quietly resisting the Credit-Copilot rollout, fearing redundancy. What do "
                 "you do?",
            "options": [
                ("Let the rollout proceed and let the manager adjust in their own time.", 0),
                ("Have a direct conversation reframing their role — from transaction-level assessment "
                 "to model-oversight and complex-case judgment — and involve them in co-designing the "
                 "transition rather than imposing it.", 3),
                ("Reassign them immediately to reduce resistance.", 1),
                ("Escalate them as a \"change blocker\" to senior management.", 0),
            ],
            "framework": "Mentoring / Subordinate Development / Transformational Management & Change "
                         "Management",
        },
        {
            "q": "As the Board pitch nears, how do you ensure the workforce/talent dimension isn't an "
                 "afterthought?",
            "options": [
                ("Leave workforce planning for after the technology decision is finalised.", 0),
                ("Insist a funded reskilling and role-redesign plan is presented alongside the "
                 "technology and competitive strategy, not after it.", 3),
                ("Assume natural attrition will resolve any redundancy concerns.", 0),
                ("Recommend a hiring freeze as the sole workforce response.", 1),
            ],
            "framework": "Managerial Leadership, Group Dynamics and Building Teams / Transformational "
                         "Management & Change Management",
        },
    ],
}

# ============================================================
# PHASE 2 — STRATEGY TABLE (budget allocation + negotiation)
# ============================================================
STRATEGIC_DIMENSIONS = {
    "AI/GenAI Credit Roadmap": [
        "Scale Credit-Copilot immediately, fix governance in parallel",
        "Phased scale-up gated on closing DPDP/bias findings first",
        "Pause GenAI underwriting; build manual capacity instead",
    ],
    "Response to NeoCred": [
        "Compete head-on on speed and pricing across the whole book",
        "Partner / embed via a Banking-as-a-Service tie-up with a fintech",
        "Defend only the premium / complex-MSME relationship segment",
    ],
    "Trade Finance Digitization": [
        "Fast-track a full-network blockchain/eBL rollout",
        "Selective pilot in top export-corridor branches",
        "Wait and watch peers prove the model first",
    ],
}

PHASE2_STANCE_PROMPT = (
    "The Board has approved a **₹300 crore, 3-year transformation budget**. Head Office needs **one "
    "unified strategic bet** covering:\n\n"
    "- Your preferred choice on each of the three strategic dimensions below\n"
    "- How you would split the ₹300 crore across them\n\n"
    "In your role, write a 2–3 sentence negotiating stance: what you will insist on, and what you are "
    "willing to trade off."
)

FACILITATOR_CHECKLIST = [
    "Listened actively to other roles before pushing own priority",
    "Was assertive without being aggressive or dismissive",
    "Grounded arguments in regulatory/ethical/business fact rather than opinion",
    "Acknowledged trade-offs explicitly rather than avoiding them",
    "Kept the discussion within the time-box",
]

# ============================================================
# PHASE 3 — BOARD PITCH
# ============================================================
BOARD_BRIEFING_PROMPT = (
    "Draft the **Board Pitch** your leadership team will deliver. It should cover, at minimum:\n\n"
    "1. Competitive diagnosis — why NeoCred is winning share, and where\n"
    "2. The strategic bet across all three dimensions, with the ₹300 crore split and rationale\n"
    "3. AI governance remediation plan — how the DPDP/bias finding will be closed, and by when\n"
    "4. Workforce/change plan — how affected staff (e.g. the Trade & MSME desk) will be supported\n"
    "5. What you are asking the Board for (approval, resources, or a decision)"
)

ACCOUNTABILITY_PROMPT = (
    "Write a short **personal accountability statement** (2–4 sentences): what you specifically own "
    "the outcome of in this strategy, and what you would do differently if a similar disruption hit "
    "again."
)

BRIEFING_KEYWORDS = {
    "AI/Gen-AI in Banking": ["genai", "gen-ai", "credit-copilot", "credit copilot", "ai model", "algorithm"],
    "DPDP Act": ["dpdp", "data protection", "consent"],
    "Ethics": ["ethic", "bias", "fair", "disparit", "transparen"],
    "Compliance & Assurance": ["complian", "audit", "remediat", "regulat"],
    "Customer Relationship Management": ["customer", "neocred", "msme", "relationship", "market share"],
    "Innovative and Digital Mindset": ["digitiz", "blockchain", "ebl", "pilot", "innovat"],
    "Change Management": ["reskill", "role-redesign", "role redesign", "change", "transition"],
    "Mentoring / Leadership": ["mentor", "manager", "team", "talent", "support"],
    "Decision-Making & Accountability": ["budget", "own", "accountab", "decision", "timeline"],
}

# ============================================================
# SESSION STATE INIT
# ============================================================
def init_state():
    defaults = {
        "team_name": "",
        "role": ROLES[0],
        "phase_idx": 0,
        "p1_answers": {},
        "p1_scores": {},
        "p2_dimension_choice": {},   # role -> {dimension: choice}
        "p2_budget": {},             # role -> {dimension: amount}
        "p2_stance": {},
        "p2_checklist": {item: False for item in FACILITATOR_CHECKLIST},
        "p3_briefing": "",
        "p3_accountability": {},
        "facilitator_mode": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("### 🏦 Simulation Controls")
    st.session_state.team_name = st.text_input("Team / Group Name", value=st.session_state.team_name)
    st.session_state.role = st.selectbox("Your Role", ROLES, index=ROLES.index(st.session_state.role))
    st.markdown("---")
    st.markdown("### Navigate Phases")
    for i, p in enumerate(PHASES):
        if st.button(p, key=f"nav_{i}", use_container_width=True,
                     type="primary" if i == st.session_state.phase_idx else "secondary"):
            st.session_state.phase_idx = i
    st.markdown("---")
    st.session_state.facilitator_mode = st.checkbox("👩‍🏫 Facilitator / Debrief View",
                                                       value=st.session_state.facilitator_mode)
    st.caption("Facilitator view reveals the scoring rubric and model answers — "
               "use only for debrief, not during live play.")

phase_idx = st.session_state.phase_idx
role = st.session_state.role

st.markdown('<p class="main-title">The Disruption Decision</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Future of Banking · Strategic Simulation · EDP for Scale IV '
            'Executives</p>', unsafe_allow_html=True)
st.markdown("---")

# ============================================================
# PHASE 0 — BRIEFING
# ============================================================
if phase_idx == 0:
    st.markdown('<div class="brief-box">' + md_to_html(SCENARIO_BRIEF) + '</div>',
                unsafe_allow_html=True)
    st.markdown(f'<div class="role-box"><b>Your Role — {role}</b><br><br>{md_to_html(ROLE_BRIEFS[role])}</div>',
                unsafe_allow_html=True)
    st.info("⏱️ Suggested timing: **10 minutes** briefing, then move to Phase 1 using the sidebar.")

# ============================================================
# PHASE 1 — DIAGNOSIS & POSITION
# ============================================================
elif phase_idx == 1:
    st.markdown('<p class="phase-header">Phase 1 · Diagnosis & Position (≈40 minutes)</p>',
                unsafe_allow_html=True)
    st.write("")
    st.markdown(f'<div class="role-box"><b>{role}</b> — {md_to_html(ROLE_BRIEFS[role])}</div>',
                unsafe_allow_html=True)

    questions = PHASE1_QUESTIONS[role]
    answers = st.session_state.p1_answers.get(role, [None] * len(questions))

    for qi, item in enumerate(questions):
        st.markdown(f"**Q{qi+1}. {item['q']}**")
        st.markdown(f'<span class="framework-tag">{item["framework"]}</span>', unsafe_allow_html=True)
        opts = [o[0] for o in item["options"]]
        default_idx = answers[qi] if answers[qi] is not None else 0
        choice = st.radio("Select the best course of action:", opts, index=default_idx,
                           key=f"p1_{role}_{qi}", label_visibility="collapsed")
        answers[qi] = opts.index(choice)
        if st.session_state.facilitator_mode:
            for oi, (text, pts) in enumerate(item["options"]):
                marker = "✅" if pts == 3 else ("⚠️" if pts >= 1 else "❌")
                st.caption(f"{marker} ({pts} pts) {text}")
        st.markdown("---")

    st.session_state.p1_answers[role] = answers

    if st.button("💾 Save Phase 1 Responses", type="primary"):
        score = sum(questions[i]["options"][a][1] for i, a in enumerate(answers) if a is not None)
        st.session_state.p1_scores[role] = score
        st.success(f"Saved. {role} scored {score} / {3 * len(questions)} on Phase 1.")

# ============================================================
# PHASE 2 — STRATEGY TABLE
# ============================================================
elif phase_idx == 2:
    st.markdown('<p class="phase-header">Phase 2 · Strategy Table — Budget & Negotiation '
                '(≈45 minutes)</p>', unsafe_allow_html=True)
    st.write("")
    st.markdown(PHASE2_STANCE_PROMPT)

    st.markdown("#### Your preferred choice on each dimension")
    choices = st.session_state.p2_dimension_choice.get(role, {})
    for dim, options in STRATEGIC_DIMENSIONS.items():
        default_idx = options.index(choices[dim]) if dim in choices and choices[dim] in options else 0
        sel = st.radio(f"**{dim}**", options, index=default_idx, key=f"p2_dim_{role}_{dim}")
        choices[dim] = sel
    st.session_state.p2_dimension_choice[role] = choices

    st.markdown("---")
    st.markdown('<div class="budget-note">💰 Split the <b>₹300 crore</b> transformation budget across '
                'the three dimensions (your individual proposal — the figures don\'t need to sum to '
                'exactly 300, the gaps are the point of the negotiation).</div>',
                unsafe_allow_html=True)
    budget = st.session_state.p2_budget.get(role, {dim: 100 for dim in STRATEGIC_DIMENSIONS})
    cols = st.columns(3)
    for i, dim in enumerate(STRATEGIC_DIMENSIONS):
        with cols[i]:
            budget[dim] = st.number_input(f"{dim} (₹ Cr)", min_value=0, max_value=300,
                                           value=int(budget.get(dim, 100)), step=10,
                                           key=f"p2_budget_{role}_{dim}")
    st.caption(f"Your proposed total: ₹{sum(budget.values())} Cr (Board-approved ceiling: ₹300 Cr)")
    st.session_state.p2_budget[role] = budget

    stance_text = st.text_area(
        "Your negotiating stance:",
        value=st.session_state.p2_stance.get(role, ""),
        height=120,
        key=f"p2_stance_{role}",
    )
    st.session_state.p2_stance[role] = stance_text

    st.markdown("---")
    st.markdown("#### 👩‍🏫 Facilitator Observation Checklist")
    st.caption("To be completed by the facilitator observing the live negotiation, not by participants.")
    for item in FACILITATOR_CHECKLIST:
        st.session_state.p2_checklist[item] = st.checkbox(
            item, value=st.session_state.p2_checklist[item], key=f"chk_{item}"
        )

    if st.button("💾 Save Phase 2 Responses", type="primary"):
        st.success(f"Saved strategic choices, budget proposal, and negotiation stance for {role}.")

# ============================================================
# PHASE 3 — BOARD PITCH
# ============================================================
elif phase_idx == 3:
    st.markdown('<p class="phase-header">Phase 3 · Board Pitch (≈35 minutes)</p>', unsafe_allow_html=True)
    st.write("")
    st.markdown(BOARD_BRIEFING_PROMPT)
    st.session_state.p3_briefing = st.text_area(
        "Team Board Pitch (one shared draft — the CSDO typically consolidates):",
        value=st.session_state.p3_briefing, height=240,
    )

    st.markdown("---")
    st.markdown(ACCOUNTABILITY_PROMPT)
    acc_text = st.text_area(
        f"Personal accountability statement — {role}:",
        value=st.session_state.p3_accountability.get(role, ""), height=100, key=f"p3_acc_{role}",
    )
    st.session_state.p3_accountability[role] = acc_text

    if st.button("💾 Save Phase 3 Responses", type="primary"):
        st.success("Saved. Proceed to the Debrief Dashboard when all teams are ready to present.")

# ============================================================
# PHASE 4 — DEBRIEF DASHBOARD
# ============================================================
elif phase_idx == 4:
    st.markdown('<p class="phase-header">Phase 4 · Debrief Dashboard</p>', unsafe_allow_html=True)
    st.write("")

    if not st.session_state.p1_scores:
        st.warning("No Phase 1 scores saved yet. Complete Phase 1 for at least one role first.")
    else:
        framework_totals = {}
        framework_max = {}
        for r, answers in st.session_state.p1_answers.items():
            qs = PHASE1_QUESTIONS[r]
            for i, a in enumerate(answers):
                if a is None:
                    continue
                fw = qs[i]["framework"]
                pts = qs[i]["options"][a][1]
                framework_totals[fw] = framework_totals.get(fw, 0) + pts
                framework_max[fw] = framework_max.get(fw, 0) + 3

        cats = list(framework_totals.keys())
        vals = [round(100 * framework_totals[c] / framework_max[c], 0) if framework_max[c] else 0
                for c in cats]

        neg_checked = sum(1 for v in st.session_state.p2_checklist.values() if v)
        neg_total = len(st.session_state.p2_checklist)
        if neg_total:
            cats = cats + ["Negotiation Behaviours"]
            vals = vals + [round(100 * neg_checked / neg_total)]

        col1, col2 = st.columns([1.3, 1])
        with col1:
            st.markdown("#### Phase 1 Scores by Role")
            for r, s in st.session_state.p1_scores.items():
                max_s = 3 * len(PHASE1_QUESTIONS[r])
                st.progress(s / max_s if max_s else 0, text=f"{r}: {s}/{max_s}")

            st.markdown("#### Framework Coverage (%)")
            if cats:
                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(r=vals, theta=cats, fill='toself',
                                               name=st.session_state.team_name or "Team"))
                fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                                   showlegend=False, height=420)
                st.plotly_chart(fig, use_container_width=True)

            st.markdown("#### Team Budget Proposals (₹ Cr) by Role")
            if st.session_state.p2_budget:
                dims = list(STRATEGIC_DIMENSIONS.keys())
                fig2 = go.Figure()
                for r, b in st.session_state.p2_budget.items():
                    fig2.add_trace(go.Bar(name=r, x=dims, y=[b.get(d, 0) for d in dims]))
                fig2.update_layout(barmode='group', height=360,
                                    yaxis_title="₹ Crore", legend=dict(orientation="h", y=-0.2))
                st.plotly_chart(fig2, use_container_width=True)
                st.caption("Wide spreads across roles are the point — that's exactly what Phase 2's "
                           "negotiation is meant to converge.")
            else:
                st.caption("No budget proposals saved yet — complete Phase 2 for at least one role.")

        with col2:
            st.markdown("#### Phase 2 — Negotiation Behaviours Observed")
            checked_count = sum(1 for v in st.session_state.p2_checklist.values() if v)
            total_count = len(st.session_state.p2_checklist)
            neg_pct = round(100 * checked_count / total_count) if total_count else 0
            st.progress(checked_count / total_count if total_count else 0,
                        text=f"Negotiation Behaviours: {checked_count}/{total_count} observed ({neg_pct}%)")
            if checked_count == 0:
                st.caption("⚠️ Not yet scored — the facilitator marks these live during Phase 2, or "
                           "retroactively here before generating the report.")
            for item, checked in st.session_state.p2_checklist.items():
                st.write(("✅ " if checked else "⬜ ") + item)
            st.markdown("**Retro-mark now (if not scored live):**")
            for item in FACILITATOR_CHECKLIST:
                st.session_state.p2_checklist[item] = st.checkbox(
                    item, value=st.session_state.p2_checklist[item], key=f"dbg_chk_{item}"
                )

            st.markdown("#### Phase 3 — Board Pitch Coverage Check")
            briefing_lower = st.session_state.p3_briefing.lower()
            for fw, kws in BRIEFING_KEYWORDS.items():
                covered = any(kw in briefing_lower for kw in kws)
                st.write(("✅ " if covered else "❌ ") + fw)

        st.markdown("---")
        st.markdown("#### 📥 Download Full Simulation Report")

        report_lines = [
            "THE DISRUPTION DECISION — Simulation Report",
            f"Team: {st.session_state.team_name or 'Unnamed'}",
            f"Generated: {datetime.now().strftime('%d %b %Y, %H:%M')}",
            "=" * 60, "",
            "PHASE 1 — DIAGNOSIS & POSITION", "-" * 40,
        ]
        for r, answers in st.session_state.p1_answers.items():
            qs = PHASE1_QUESTIONS[r]
            report_lines.append(f"\nRole: {r}  (Score: {st.session_state.p1_scores.get(r, 'n/a')})")
            for i, a in enumerate(answers):
                if a is None:
                    continue
                report_lines.append(f"  Q{i+1}: {qs[i]['q']}")
                report_lines.append(f"    Chosen: {qs[i]['options'][a][0]} ({qs[i]['options'][a][1]} pts)")
                report_lines.append(f"    Framework: {qs[i]['framework']}")

        report_lines += ["", "PHASE 2 — STRATEGY TABLE", "-" * 40]
        for r, stance in st.session_state.p2_stance.items():
            report_lines.append(f"\nRole: {r}")
            dims = st.session_state.p2_dimension_choice.get(r, {})
            for d, c in dims.items():
                report_lines.append(f"  {d}: {c}")
            b = st.session_state.p2_budget.get(r, {})
            if b:
                report_lines.append(f"  Budget proposal (₹ Cr): " +
                                     ", ".join(f"{k}={v}" for k, v in b.items()) +
                                     f"  [Total: {sum(b.values())}]")
            report_lines.append(f"  Stance: {stance}")
        _neg_checked = sum(1 for v in st.session_state.p2_checklist.values() if v)
        _neg_total = len(st.session_state.p2_checklist)
        report_lines.append(f"\nFacilitator-observed behaviours "
                             f"({_neg_checked}/{_neg_total} observed, "
                             f"{round(100*_neg_checked/_neg_total) if _neg_total else 0}%):")
        for item, checked in st.session_state.p2_checklist.items():
            report_lines.append(f"  [{'x' if checked else ' '}] {item}")

        report_lines += ["", "PHASE 3 — BOARD PITCH", "-" * 40]
        report_lines.append(f"\nBoard Pitch:\n{st.session_state.p3_briefing}")
        report_lines.append("\nAccountability Statements:")
        for r, acc in st.session_state.p3_accountability.items():
            report_lines.append(f"  {r}: {acc}")

        report_text = "\n".join(report_lines)
        st.download_button(
            "⬇️ Download Report (.txt)",
            data=io.BytesIO(report_text.encode("utf-8")),
            file_name=f"disruption_decision_{(st.session_state.team_name or 'team').replace(' ', '_')}.txt",
            mime="text/plain",
        )

    st.markdown("---")
    st.markdown("#### 🎯 Facilitator Debrief Talking Points")
    st.markdown("""
- **AI/Gen-AI & Ethics**: Did the team treat the DPDP/bias finding as a genuine gate on scale-up, or
  as a footnote to the growth story? Did anyone propose shipping the fix *after* scaling?
- **Decision-Making & Accountability**: Did the CSDO integrate the governance and people issues into
  the core strategy, or let them run as side conversations?
- **Innovative & Digital Mindset**: Was the trade-finance digitization choice a genuine build-vs-partner
  judgment, or a reflexive "wait and see"?
- **Customer Relationship Management**: Did the team distinguish between the segments genuinely at risk
  from NeoCred and the ones where price-cutting would simply erode margin for no retention gain?
- **Change Management / Mentoring**: Did HR's response to the senior Trade & MSME manager reframe their
  role, or just manage the optics of resistance?
- **Negotiation**: How wide was the spread between roles' budget proposals before the Phase 2
  conversation — and did the final Board Pitch actually converge, or did one function's number simply
  win by default?
- **Synthesis across the EDP**: Does this pitch draw on frameworks from earlier in the program (AI
  governance, compliance, change management) or treat "Future of Banking" as a purely commercial topic?
""")

st.markdown("---")
st.caption("Future of Banking Strategic Simulation · Designed for IIM Tiruchirappalli, Department of "
           "Finance · Deploy one instance per team/breakout group.")
