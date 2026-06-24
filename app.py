import random
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Number Hunt",
    page_icon="🎯",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

/* ── Reset & base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #0d0f14 !important;
    color: #e8eaf0 !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none !important; }
.block-container { padding: 2.5rem 1.5rem 4rem !important; max-width: 560px !important; }

/* ── Title card ── */
.title-card {
    text-align: center;
    padding: 2.4rem 2rem 2rem;
    background: linear-gradient(145deg, #161923, #1c2030);
    border: 1px solid #2a2f40;
    border-radius: 20px;
    margin-bottom: 1.6rem;
    position: relative;
    overflow: hidden;
}
.title-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% -30%, rgba(99,102,241,.18) 0%, transparent 70%);
    pointer-events: none;
}
.game-title {
    font-family: 'Space Mono', monospace;
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: -1px;
    color: #fff;
    margin: 0 0 .3rem;
}
.game-title span { color: #818cf8; }
.game-subtitle {
    font-size: .92rem;
    color: #6b7280;
    letter-spacing: .04em;
}

/* ── Stat pills ── */
.stats-row {
    display: flex;
    gap: .75rem;
    margin-bottom: 1.6rem;
}
.stat-pill {
    flex: 1;
    background: #161923;
    border: 1px solid #2a2f40;
    border-radius: 12px;
    padding: .9rem .5rem;
    text-align: center;
}
.stat-value {
    font-family: 'Space Mono', monospace;
    font-size: 1.5rem;
    font-weight: 700;
    color: #818cf8;
    line-height: 1;
}
.stat-label {
    font-size: .7rem;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: .08em;
    margin-top: .25rem;
}

/* ── Range indicator ── */
.range-bar-wrap {
    background: #161923;
    border: 1px solid #2a2f40;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1.5rem;
    position: relative;
}
.range-label {
    font-size: .75rem;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: .08em;
    margin-bottom: .6rem;
}
.range-track {
    height: 6px;
    background: #1f2433;
    border-radius: 99px;
    position: relative;
    overflow: hidden;
}
.range-fill {
    height: 100%;
    background: linear-gradient(90deg, #818cf8, #c084fc);
    border-radius: 99px;
    transition: width .4s ease;
}
.range-bounds {
    display: flex;
    justify-content: space-between;
    font-family: 'Space Mono', monospace;
    font-size: .8rem;
    color: #9ca3af;
    margin-top: .5rem;
}

/* ── Input box ── */
div[data-testid="stNumberInput"] {
    margin-bottom: .5rem !important;
}
div[data-testid="stNumberInput"] label {
    font-size: .8rem !important;
    color: #9ca3af !important;
    text-transform: uppercase !important;
    letter-spacing: .07em !important;
    margin-bottom: .35rem !important;
    display: block;
}
div[data-testid="stNumberInput"] input {
    background: #161923 !important;
    border: 1.5px solid #2a2f40 !important;
    border-radius: 12px !important;
    color: #fff !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 1.25rem !important;
    padding: .75rem 1rem !important;
    transition: border-color .2s;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: #818cf8 !important;
    box-shadow: 0 0 0 3px rgba(129,140,248,.12) !important;
}
/* hide +/- steppers */
div[data-testid="stNumberInput"] button { display: none !important; }

/* ── Primary button ── */
div[data-testid="stButton"] > button {
    width: 100% !important;
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    padding: .85rem 0 !important;
    letter-spacing: .02em !important;
    transition: filter .2s, transform .1s !important;
    cursor: pointer !important;
    margin-top: .25rem !important;
}
div[data-testid="stButton"] > button:hover {
    filter: brightness(1.12) !important;
    transform: translateY(-1px) !important;
}
div[data-testid="stButton"] > button:active { transform: translateY(0) !important; }

/* ── Feedback strip ── */
.feedback-strip {
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin: 1rem 0;
    font-weight: 600;
    font-size: .95rem;
    display: flex;
    align-items: center;
    gap: .6rem;
    animation: slideUp .3s ease;
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}
.feedback-low  { background: rgba(239,68,68,.12);  border: 1px solid rgba(239,68,68,.3);  color: #fca5a5; }
.feedback-high { background: rgba(249,115,22,.12); border: 1px solid rgba(249,115,22,.3); color: #fdba74; }
.feedback-win  { background: rgba(34,197,94,.12);  border: 1px solid rgba(34,197,94,.3);  color: #86efac; }
.feedback-lose { background: rgba(239,68,68,.12);  border: 1px solid rgba(239,68,68,.3);  color: #fca5a5; }

/* ── History log ── */
.history-wrap {
    background: #161923;
    border: 1px solid #2a2f40;
    border-radius: 14px;
    padding: 1rem 1.2rem;
    margin-top: 1.2rem;
    max-height: 200px;
    overflow-y: auto;
}
.history-title {
    font-size: .72rem;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: .09em;
    margin-bottom: .7rem;
}
.history-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: .35rem 0;
    border-bottom: 1px solid #1f2433;
    font-family: 'Space Mono', monospace;
    font-size: .82rem;
}
.history-row:last-child { border-bottom: none; }
.h-attempt { color: #6b7280; }
.h-guess   { color: #e8eaf0; font-weight: 700; }
.h-verdict { font-size: .75rem; }
.v-low  { color: #fca5a5; }
.v-high { color: #fdba74; }
.v-win  { color: #86efac; }

/* ── Play-again / Reset button (secondary style) ── */
.reset-hint {
    text-align: center;
    font-size: .8rem;
    color: #4b5563;
    margin-top: 1.2rem;
    letter-spacing: .03em;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #2a2f40; border-radius: 99px; }
</style>
""", unsafe_allow_html=True)


# ── Session state init ────────────────────────────────────────────────────────
MAX_ATTEMPTS = 7

def new_game():
    st.session_state.secret   = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.history  = []          # list of (attempt, guess, verdict)
    st.session_state.lo       = 1
    st.session_state.hi       = 100
    st.session_state.status   = "playing"   # "playing" | "won" | "lost"
    st.session_state.feedback = None
    st.session_state.last_guess = None

if "secret" not in st.session_state:
    new_game()


# ── Title ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-card">
  <div class="game-title">NUMBER <span>HUNT</span></div>
  <div class="game-subtitle">Guess the secret number · 1 to 100</div>
</div>
""", unsafe_allow_html=True)


# ── Stats row ─────────────────────────────────────────────────────────────────
attempts_left = MAX_ATTEMPTS - st.session_state.attempts
st.markdown(f"""
<div class="stats-row">
  <div class="stat-pill">
    <div class="stat-value">{st.session_state.attempts}</div>
    <div class="stat-label">Guesses</div>
  </div>
  <div class="stat-pill">
    <div class="stat-value">{attempts_left}</div>
    <div class="stat-label">Remaining</div>
  </div>
  <div class="stat-pill">
    <div class="stat-value">{st.session_state.lo}–{st.session_state.hi}</div>
    <div class="stat-label">Range</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Range bar ─────────────────────────────────────────────────────────────────
range_pct = max(0, round(
    (1 - (st.session_state.hi - st.session_state.lo) / 99) * 100
))
st.markdown(f"""
<div class="range-bar-wrap">
  <div class="range-label">Narrowed down</div>
  <div class="range-track">
    <div class="range-fill" style="width:{range_pct}%"></div>
  </div>
  <div class="range-bounds">
    <span>{st.session_state.lo}</span>
    <span>{range_pct}% eliminated</span>
    <span>{st.session_state.hi}</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Game area ─────────────────────────────────────────────────────────────────
if st.session_state.status == "playing":
    guess = st.number_input(
        "Your guess",
        min_value=1,
        max_value=100,
        step=1,
        value=None,
        placeholder="Enter 1 – 100",
        key="guess_input",
        label_visibility="visible",
    )

    if st.button("🎯  Lock In Guess"):
        if guess is None:
            st.warning("Enter a number first.")
        else:
            guess = int(guess)
            st.session_state.attempts += 1
            st.session_state.last_guess = guess

            if guess == st.session_state.secret:
                st.session_state.status   = "won"
                st.session_state.feedback = "win"
                st.session_state.history.append((st.session_state.attempts, guess, "win"))

            elif st.session_state.attempts >= MAX_ATTEMPTS:
                st.session_state.status   = "lost"
                st.session_state.feedback = "lose"
                st.session_state.history.append((st.session_state.attempts, guess,
                                                  "low" if guess < st.session_state.secret else "high"))

            elif guess < st.session_state.secret:
                st.session_state.feedback = "low"
                st.session_state.lo       = max(st.session_state.lo, guess + 1)
                st.session_state.history.append((st.session_state.attempts, guess, "low"))

            else:
                st.session_state.feedback = "high"
                st.session_state.hi       = min(st.session_state.hi, guess - 1)
                st.session_state.history.append((st.session_state.attempts, guess, "high"))

            st.rerun()


# ── Feedback strip ────────────────────────────────────────────────────────────
fb = st.session_state.feedback
if fb == "low":
    st.markdown(f'<div class="feedback-strip feedback-low">📈 Too low — aim higher than <b>{st.session_state.last_guess}</b></div>', unsafe_allow_html=True)
elif fb == "high":
    st.markdown(f'<div class="feedback-strip feedback-high">📉 Too high — aim lower than <b>{st.session_state.last_guess}</b></div>', unsafe_allow_html=True)
elif fb == "win":
    st.markdown(f'<div class="feedback-strip feedback-win">🎉 Nailed it! <b>{st.session_state.secret}</b> was the number — found in {st.session_state.attempts} guess{"es" if st.session_state.attempts != 1 else ""}</div>', unsafe_allow_html=True)
elif fb == "lose":
    st.markdown(f'<div class="feedback-strip feedback-lose">💀 Out of guesses — the number was <b>{st.session_state.secret}</b></div>', unsafe_allow_html=True)


# ── End-game balloons ─────────────────────────────────────────────────────────
if st.session_state.status == "won":
    st.balloons()
elif st.session_state.status == "lost":
    st.snow()   # snow = loss effect (Streamlit's built-in alternative)


# ── Guess history ─────────────────────────────────────────────────────────────
if st.session_state.history:
    rows_html = ""
    for attempt, guess, verdict in reversed(st.session_state.history):
        v_class = {"low": "v-low", "high": "v-high", "win": "v-win", "lose": "v-low"}.get(verdict, "")
        v_label = {"low": "↑ Too low", "high": "↓ Too high", "win": "✓ Correct", "lose": "↑ Too low/high"}.get(verdict, "")
        rows_html += f"""
        <div class="history-row">
          <span class="h-attempt">#{attempt}</span>
          <span class="h-guess">{guess}</span>
          <span class="h-verdict {v_class}">{v_label}</span>
        </div>"""
    st.markdown(f'<div class="history-wrap"><div class="history-title">Guess log</div>{rows_html}</div>', unsafe_allow_html=True)


# ── Reset ─────────────────────────────────────────────────────────────────────
if st.session_state.status in ("won", "lost"):
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄  Play Again"):
        new_game()
        st.rerun()
else:
    st.markdown('<div class="reset-hint">Max 7 guesses · hit Play Again any time to reset</div>', unsafe_allow_html=True)
    if st.button("↩  Reset Game"):
        new_game()
        st.rerun()