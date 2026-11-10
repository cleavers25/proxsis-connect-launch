import os
import subprocess

OUTPUT_DIR = "/home/cleavers/Dokumen/coolify_new/poster_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. FEED PORTRAIT POSTER (1080 x 1350) - 4:5 Ratio
# -------------------------------------------------------------
html_portrait = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1350, initial-scale=1.0">
<title>Poster Countdown Coolify - Proxsis Connect (Portrait)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    width: 1080px;
    height: 1350px;
    background-color: #070913;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 64px 72px 56px 72px;
  }

  /* Ambient Glows & Background Graphics */
  .bg-glow-top {
    position: absolute;
    top: -120px;
    right: -80px;
    width: 650px;
    height: 650px;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.35) 0%, rgba(139, 92, 246, 0.15) 45%, transparent 70%);
    filter: blur(80px);
    pointer-events: none;
    z-index: 0;
  }

  .bg-glow-bottom {
    position: absolute;
    bottom: -150px;
    left: -100px;
    width: 700px;
    height: 700px;
    background: radial-gradient(circle, rgba(14, 165, 233, 0.3) 0%, rgba(56, 189, 248, 0.1) 50%, transparent 75%);
    filter: blur(90px);
    pointer-events: none;
    z-index: 0;
  }

  .bg-glow-center {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 500px;
    height: 400px;
    background: radial-gradient(circle, rgba(168, 85, 247, 0.2) 0%, transparent 70%);
    filter: blur(100px);
    pointer-events: none;
    z-index: 0;
  }

  /* Grid overlay */
  .cyber-grid {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 48px 48px;
    mask-image: radial-gradient(ellipse 90% 80% at 50% 50%, black 40%, transparent 95%);
    -webkit-mask-image: radial-gradient(ellipse 90% 80% at 50% 50%, black 40%, transparent 95%);
    pointer-events: none;
    z-index: 1;
  }

  .content-layer {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
  }

  /* HEADER */
  .poster-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .brand-group {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .brand-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #6366f1, #38bdf8);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 24px rgba(99, 102, 241, 0.5);
  }

  .brand-icon svg {
    width: 26px;
    height: 26px;
    fill: #ffffff;
  }

  .brand-title {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #ffffff;
  }

  .brand-subtitle {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #94a3b8;
    text-transform: uppercase;
  }

  .live-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 18px;
    border-radius: 999px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(52, 211, 153, 0.35);
    backdrop-filter: blur(12px);
  }

  .live-dot {
    width: 10px;
    height: 10px;
    background-color: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 12px #34d399, 0 0 20px #10b981;
  }

  .live-text {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.1em;
    color: #34d399;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
  }

  /* COUNTDOWN HERO SECTION */
  .countdown-hero {
    margin-top: 24px;
    margin-bottom: 20px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .countdown-badge-wrapper {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
  }

  .countdown-pill {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 24px;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(129, 140, 248, 0.4);
    border-radius: 100px;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.2);
  }

  .countdown-pill svg {
    width: 18px;
    height: 18px;
    fill: #818cf8;
  }

  .countdown-pill span {
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.15em;
    color: #c7d2fe;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
  }

  .countdown-headline {
    font-size: 76px;
    line-height: 1.02;
    font-weight: 900;
    letter-spacing: -0.03em;
    text-transform: uppercase;
    margin-bottom: 12px;
  }

  .gradient-text-fire {
    background: linear-gradient(135deg, #ffffff 10%, #f1f5f9 40%, #38bdf8 70%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .gradient-text-accent {
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .teaser-quote {
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 14px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 8px 24px;
    border-radius: 100px;
    backdrop-filter: blur(10px);
    margin-top: 6px;
  }

  .teaser-quote .highlight {
    color: #38bdf8;
    font-weight: 800;
  }

  .teaser-quote .dot {
    color: #818cf8;
  }

  /* PIPELINE PREVIEW CARD */
  .pipeline-card {
    background: rgba(15, 23, 42, 0.72);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 24px;
    padding: 26px 30px;
    box-shadow: 0 24px 60px -12px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(24px);
    margin-top: 10px;
  }

  .terminal-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 18px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 20px;
  }

  .window-dots {
    display: flex;
    gap: 8px;
  }

  .w-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }

  .w-dot.red { background: #ef4444; }
  .w-dot.yellow { background: #f59e0b; }
  .w-dot.green { background: #10b981; }

  .terminal-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #94a3b8;
    letter-spacing: 0.04em;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .terminal-title .url-highlight {
    color: #38bdf8;
    font-weight: 600;
  }

  .branch-tag {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.25);
    padding: 4px 10px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #38bdf8;
  }

  /* PIPELINE STEPS */
  .pipeline-flow {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 16px;
    margin-bottom: 22px;
  }

  .step-box {
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    position: relative;
    overflow: hidden;
  }

  .step-box.active {
    border-color: rgba(56, 189, 248, 0.4);
    background: linear-gradient(180deg, rgba(56, 189, 248, 0.08) 0%, rgba(30, 41, 59, 0.6) 100%);
  }

  .step-box.success {
    border-color: rgba(52, 211, 153, 0.4);
    background: linear-gradient(180deg, rgba(52, 211, 153, 0.08) 0%, rgba(30, 41, 59, 0.6) 100%);
  }

  .step-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .step-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
  }

  .step-status-icon {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .step-box.success .step-status-icon {
    background: #10b981;
    color: #ffffff;
  }

  .step-box.active .step-status-icon {
    background: #0284c7;
    color: #ffffff;
  }

  .step-title {
    font-size: 15px;
    font-weight: 700;
    color: #f1f5f9;
  }

  .step-desc {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.3;
  }

  /* CONSOLE LOG BAR */
  .console-strip {
    background: #090d16;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
  }

  .console-cmd {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #cbd5e1;
  }

  .console-prompt {
    color: #10b981;
    font-weight: 700;
  }

  .console-badge {
    background: rgba(16, 185, 129, 0.15);
    color: #34d399;
    padding: 3px 8px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 11px;
    letter-spacing: 0.05em;
  }

  /* BODY COPY & SUMMARY */
  .copywriting-box {
    margin-top: 18px;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.03) 0%, rgba(255, 255, 255, 0.01) 100%);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 20px;
    padding: 22px 28px;
  }

  .copy-headline {
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 0.02em;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .copy-headline svg {
    width: 20px;
    height: 20px;
    fill: #38bdf8;
  }

  .copy-body {
    font-size: 15px;
    line-height: 1.55;
    color: #cbd5e1;
  }

  .copy-body strong {
    color: #f8fafc;
    font-weight: 700;
  }

  /* FOOTER EVENT INFO */
  .poster-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(11, 15, 25, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 20px 28px;
    backdrop-filter: blur(20px);
  }

  .date-block {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .date-calendar-icon {
    width: 52px;
    height: 52px;
    background: linear-gradient(135deg, #4f46e5, #06b6d4);
    border-radius: 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 20px rgba(6, 182, 212, 0.25);
  }

  .cal-month {
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    color: #e0f2fe;
    letter-spacing: 0.1em;
  }

  .cal-day {
    font-size: 22px;
    font-weight: 900;
    color: #ffffff;
    line-height: 1;
  }

  .date-details {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .date-main {
    font-size: 19px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.01em;
  }

  .date-sub {
    font-size: 13px;
    color: #94a3b8;
    font-weight: 500;
  }

  .action-block {
    text-align: right;
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: flex-end;
  }

  .portal-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.35);
    padding: 8px 16px;
    border-radius: 100px;
  }

  .portal-pill span {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
    font-weight: 700;
    color: #38bdf8;
  }

  .hashtags {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #64748b;
    letter-spacing: 0.05em;
  }
</style>
</head>
<body>

  <!-- Ambient background glow & grid -->
  <div class="bg-glow-top"></div>
  <div class="bg-glow-bottom"></div>
  <div class="bg-glow-center"></div>
  <div class="cyber-grid"></div>

  <div class="content-layer">
    <!-- 1. HEADER -->
    <header class="poster-header">
      <div class="brand-group">
        <div class="brand-icon">
          <!-- Rocket/Deploy Icon -->
          <svg viewBox="0 0 24 24">
            <path d="M12 2.5s4 4 4 10.5c0 2.5-1.5 4.5-4 5.5-2.5-1-4-3-4-5.5 0-6.5 4-10.5 4-10.5z"/>
            <path d="M5 13c-2 2-2 5-2 5s3 0 5-2"/>
            <path d="M19 13c2 2 2 5 2 5s-3 0-5-2"/>
            <circle cx="12" cy="9" r="1.5" fill="#070913"/>
          </svg>
        </div>
        <div>
          <div class="brand-title">Proxsis Connect</div>
          <div class="brand-subtitle">Cloud PaaS • Powered by Coolify</div>
        </div>
      </div>

      <div class="live-pill">
        <div class="live-dot"></div>
        <div class="live-text">Live Demo Soon</div>
      </div>
    </header>

    <!-- 2. COUNTDOWN HERO -->
    <section class="countdown-hero">
      <div class="countdown-badge-wrapper">
        <div class="countdown-pill">
          <svg viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" fill="none"/>
            <polyline points="12 6 12 12 16 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/>
          </svg>
          <span>Official Countdown</span>
        </div>
      </div>

      <h1 class="countdown-headline">
        <span class="gradient-text-fire">TOMORROW,</span><br>
        <span class="gradient-text-accent">WE GO LIVE!</span>
      </h1>

      <div class="teaser-quote">
        <span>“See it <span class="highlight">built</span>.</span>
        <span class="dot">•</span>
        <span>See it <span class="highlight">deployed</span>.”</span>
      </div>
    </section>

    <!-- 3. INTERACTIVE PIPELINE / TERMINAL PREVIEW CARD -->
    <div class="pipeline-card">
      <div class="terminal-topbar">
        <div class="window-dots">
          <div class="w-dot red"></div>
          <div class="w-dot yellow"></div>
          <div class="w-dot green"></div>
        </div>
        <div class="terminal-title">
          <span>Deployment Engine •</span>
          <span class="url-highlight">connect.proxsis.com</span>
        </div>
        <div class="branch-tag">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <line x1="6" y1="3" x2="6" y2="15"></line>
            <circle cx="18" cy="6" r="3"></circle>
            <circle cx="6" cy="18" r="3"></circle>
            <path d="M18 9a9 9 0 0 1-9 9"></path>
          </svg>
          main
        </div>
      </div>

      <!-- 3 Steps of Coolify Workflow -->
      <div class="pipeline-flow">
        <div class="step-box success">
          <div class="step-header">
            <span class="step-num">Step 01</span>
            <div class="step-status-icon">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
          </div>
          <div class="step-title">Source & Build</div>
          <div class="step-desc">Git Push auto-trigger Docker image compilation</div>
        </div>

        <div class="step-box success">
          <div class="step-header">
            <span class="step-num">Step 02</span>
            <div class="step-status-icon">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
          </div>
          <div class="step-title">Self-Hosted PaaS</div>
          <div class="step-desc">Orkestrasi kontainer aman di on-premise Proxmox</div>
        </div>

        <div class="step-box active">
          <div class="step-header">
            <span class="step-num">Step 03</span>
            <div class="step-status-icon">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
                <circle cx="12" cy="12" r="5"></circle>
              </svg>
            </div>
          </div>
          <div class="step-title">Live Production</div>
          <div class="step-desc">Instant SSL & Domain siap diakses dalam hitungan detik</div>
        </div>
      </div>

      <!-- Console output bar -->
      <div class="console-strip">
        <div class="console-cmd">
          <span class="console-prompt">$</span>
          <span>coolify deploy --app "proxsis-app" --env production</span>
        </div>
        <div class="console-badge">✓ BUILD SUCCESS (1.2s)</div>
      </div>
    </div>

    <!-- 4. SCRIPT & COPYWRITING NARRATIVE -->
    <div class="copywriting-box">
      <div class="copy-headline">
        <svg viewBox="0 0 24 24">
          <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
        </svg>
        <span>Live Demonstration & Platform Walkthrough</span>
      </div>
      <p class="copy-body">
        Besok, kita akan mengenal <strong>Proxsis Connect</strong> lebih dekat dan melihat langsung bagaimana aplikasi bisa di-deploy dengan cepat & mandiri. Dari proses <em>build</em> otomatis hingga aplikasi siap diakses secara publik. <strong>Jangan lewatkan live demo-nya!</strong>
      </p>
    </div>

    <!-- 5. FOOTER EVENT INFO -->
    <footer class="poster-footer">
      <div class="date-block">
        <div class="date-calendar-icon">
          <span class="cal-month">NOV</span>
          <span class="cal-day">11</span>
        </div>
        <div class="date-details">
          <div class="date-main">Rabu, 11 November 2026</div>
          <div class="date-sub">Sesi Sosialisasi & Hands-On Demo • Live Session</div>
        </div>
      </div>

      <div class="action-block">
        <div class="portal-pill">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2.5">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
          <span>connect.proxsis.com</span>
        </div>
        <div class="hashtags">#ProxsisConnect #Coolify #LaunchDay</div>
      </div>
    </footer>
  </div>

</body>
</html>
"""

# -------------------------------------------------------------
# 2. FEED SQUARE POSTER (1080 x 1080) - 1:1 Ratio
# -------------------------------------------------------------
html_square = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1080, initial-scale=1.0">
<title>Poster Countdown Coolify - Proxsis Connect (Square 1:1)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    width: 1080px;
    height: 1080px;
    background-color: #070913;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 56px 64px 48px 64px;
  }

  .bg-glow-top {
    position: absolute;
    top: -100px;
    right: -60px;
    width: 550px;
    height: 550px;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.35) 0%, rgba(139, 92, 246, 0.15) 45%, transparent 70%);
    filter: blur(80px);
    pointer-events: none;
    z-index: 0;
  }

  .bg-glow-bottom {
    position: absolute;
    bottom: -100px;
    left: -80px;
    width: 550px;
    height: 550px;
    background: radial-gradient(circle, rgba(14, 165, 233, 0.3) 0%, transparent 75%);
    filter: blur(90px);
    pointer-events: none;
    z-index: 0;
  }

  .cyber-grid {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 44px 44px;
    mask-image: radial-gradient(ellipse 90% 80% at 50% 50%, black 40%, transparent 95%);
    -webkit-mask-image: radial-gradient(ellipse 90% 80% at 50% 50%, black 40%, transparent 95%);
    pointer-events: none;
    z-index: 1;
  }

  .content-layer {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
  }

  .poster-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .brand-group {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .brand-icon {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #6366f1, #38bdf8);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
  }

  .brand-icon svg { width: 24px; height: 24px; fill: #ffffff; }

  .brand-title {
    font-size: 19px;
    font-weight: 800;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #ffffff;
  }

  .brand-subtitle {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #94a3b8;
    text-transform: uppercase;
  }

  .live-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 7px 16px;
    border-radius: 999px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(52, 211, 153, 0.35);
  }

  .live-dot {
    width: 8px;
    height: 8px;
    background-color: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 10px #34d399;
  }

  .live-text {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: #34d399;
    font-family: 'JetBrains Mono', monospace;
  }

  .countdown-hero {
    text-align: center;
    margin: 10px 0;
  }

  .countdown-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 7px 20px;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(129, 140, 248, 0.4);
    border-radius: 100px;
    margin-bottom: 12px;
  }

  .countdown-pill span {
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #c7d2fe;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
  }

  .countdown-headline {
    font-size: 64px;
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -0.03em;
    text-transform: uppercase;
    margin-bottom: 12px;
  }

  .gradient-text-fire {
    background: linear-gradient(135deg, #ffffff 10%, #f1f5f9 40%, #38bdf8 70%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .gradient-text-accent {
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .teaser-quote {
    font-size: 24px;
    font-weight: 700;
    color: #e2e8f0;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 7px 20px;
    border-radius: 100px;
  }

  .teaser-quote .highlight { color: #38bdf8; font-weight: 800; }

  /* CARDS GRID */
  .middle-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 18px;
    align-items: stretch;
    margin: 10px 0;
  }

  .terminal-card {
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(20px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .terminal-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 14px;
  }

  .window-dots { display: flex; gap: 6px; }
  .w-dot { width: 10px; height: 10px; border-radius: 50%; }
  .w-dot.red { background: #ef4444; }
  .w-dot.yellow { background: #f59e0b; }
  .w-dot.green { background: #10b981; }

  .terminal-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #38bdf8;
    font-weight: 600;
  }

  .pipeline-steps-mini {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .p-step {
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.05);
    padding: 10px 14px;
    border-radius: 12px;
  }

  .p-step.success { border-color: rgba(52, 211, 153, 0.3); }

  .p-icon {
    width: 24px;
    height: 24px;
    background: #10b981;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .p-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #e2e8f0;
  }

  .p-text strong { color: #38bdf8; }

  .copy-card {
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 12px;
  }

  .copy-card-title {
    font-size: 16px;
    font-weight: 800;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .copy-card-title svg { width: 18px; height: 18px; fill: #38bdf8; }

  .copy-card-text {
    font-size: 13.5px;
    line-height: 1.5;
    color: #cbd5e1;
  }

  .copy-card-text strong { color: #f1f5f9; }

  .poster-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(11, 15, 25, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 18px;
    padding: 18px 24px;
    backdrop-filter: blur(16px);
  }

  .date-block { display: flex; align-items: center; gap: 14px; }

  .date-calendar-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #4f46e5, #06b6d4);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .cal-month { font-size: 9px; font-weight: 800; color: #e0f2fe; letter-spacing: 0.1em; }
  .cal-day { font-size: 20px; font-weight: 900; color: #ffffff; line-height: 1; }

  .date-main { font-size: 17px; font-weight: 800; color: #ffffff; }
  .date-sub { font-size: 12px; color: #94a3b8; }

  .action-block { text-align: right; }
  .portal-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.35);
    padding: 7px 14px;
    border-radius: 100px;
    margin-bottom: 4px;
  }

  .portal-pill span {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 700;
    color: #38bdf8;
  }

  .hashtags {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    color: #64748b;
  }
</style>
</head>
<body>
  <div class="bg-glow-top"></div>
  <div class="bg-glow-bottom"></div>
  <div class="cyber-grid"></div>

  <div class="content-layer">
    <header class="poster-header">
      <div class="brand-group">
        <div class="brand-icon">
          <svg viewBox="0 0 24 24">
            <path d="M12 2.5s4 4 4 10.5c0 2.5-1.5 4.5-4 5.5-2.5-1-4-3-4-5.5 0-6.5 4-10.5 4-10.5z"/>
            <path d="M5 13c-2 2-2 5-2 5s3 0 5-2"/>
            <path d="M19 13c2 2 2 5 2 5s-3 0-5-2"/>
          </svg>
        </div>
        <div>
          <div class="brand-title">Proxsis Connect</div>
          <div class="brand-subtitle">Cloud PaaS • Powered by Coolify</div>
        </div>
      </div>
      <div class="live-pill">
        <div class="live-dot"></div>
        <div class="live-text">Live Demo Soon</div>
      </div>
    </header>

    <section class="countdown-hero">
      <div class="countdown-pill">
        <span>⏱️ Official Countdown</span>
      </div>
      <h1 class="countdown-headline">
        <span class="gradient-text-fire">TOMORROW,</span><br>
        <span class="gradient-text-accent">WE GO LIVE!</span>
      </h1>
      <div class="teaser-quote">
        <span>“See it <span class="highlight">built</span>. See it <span class="highlight">deployed</span>.”</span>
      </div>
    </section>

    <div class="middle-grid">
      <div class="terminal-card">
        <div class="terminal-topbar">
          <div class="window-dots">
            <div class="w-dot red"></div>
            <div class="w-dot yellow"></div>
            <div class="w-dot green"></div>
          </div>
          <div class="terminal-title">connect.proxsis.com</div>
        </div>
        <div class="pipeline-steps-mini">
          <div class="p-step success">
            <div class="p-icon">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
            <div class="p-text"><strong>Git Push:</strong> Automatic Build Pipeline</div>
          </div>
          <div class="p-step success">
            <div class="p-icon">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
            <div class="p-text"><strong>Container:</strong> Self-Hosted on Proxmox</div>
          </div>
          <div class="p-step success">
            <div class="p-icon">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
            <div class="p-text"><strong>Status:</strong> Live with SSL in seconds</div>
          </div>
        </div>
      </div>

      <div class="copy-card">
        <div class="copy-card-title">
          <svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
          <span>Live Demo Besok!</span>
        </div>
        <p class="copy-card-text">
          Melihat langsung bagaimana aplikasi di-deploy dari kode sumber hingga live production. Dilengkapi live demo workflow deployment Coolify.
        </p>
      </div>
    </div>

    <footer class="poster-footer">
      <div class="date-block">
        <div class="date-calendar-icon">
          <span class="cal-month">NOV</span>
          <span class="cal-day">11</span>
        </div>
        <div class="date-details">
          <div class="date-main">Rabu, 11 November 2026</div>
          <div class="date-sub">Sesi Live Sosialisasi & Demo Coolify</div>
        </div>
      </div>
      <div class="action-block">
        <div class="portal-pill">
          <span>connect.proxsis.com</span>
        </div>
        <div class="hashtags">#ProxsisConnect #Coolify #LaunchDay</div>
      </div>
    </footer>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------
# 3. STORY VERTICAL POSTER (1080 x 1920) - 9:16 Ratio
# -------------------------------------------------------------
html_story = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920, initial-scale=1.0">
<title>Poster Countdown Coolify - Proxsis Connect (Story 9:16)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    width: 1080px;
    height: 1920px;
    background-color: #070913;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    color: #f8fafc;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 100px 72px 90px 72px;
  }

  .bg-glow-top {
    position: absolute;
    top: -150px;
    right: -100px;
    width: 750px;
    height: 750px;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.4) 0%, rgba(139, 92, 246, 0.2) 45%, transparent 70%);
    filter: blur(100px);
    pointer-events: none;
    z-index: 0;
  }

  .bg-glow-bottom {
    position: absolute;
    bottom: -150px;
    left: -100px;
    width: 750px;
    height: 750px;
    background: radial-gradient(circle, rgba(14, 165, 233, 0.35) 0%, transparent 75%);
    filter: blur(100px);
    pointer-events: none;
    z-index: 0;
  }

  .cyber-grid {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(to right, rgba(255, 255, 255, 0.035) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.035) 1px, transparent 1px);
    background-size: 52px 52px;
    mask-image: radial-gradient(ellipse 90% 80% at 50% 50%, black 40%, transparent 95%);
    -webkit-mask-image: radial-gradient(ellipse 90% 80% at 50% 50%, black 40%, transparent 95%);
    pointer-events: none;
    z-index: 1;
  }

  .content-layer {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
  }

  .poster-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .brand-group {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .brand-icon {
    width: 54px;
    height: 54px;
    background: linear-gradient(135deg, #6366f1, #38bdf8);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 24px rgba(99, 102, 241, 0.5);
  }

  .brand-icon svg { width: 30px; height: 30px; fill: #ffffff; }

  .brand-title {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #ffffff;
  }

  .brand-subtitle {
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #94a3b8;
    text-transform: uppercase;
  }

  .live-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 22px;
    border-radius: 999px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(52, 211, 153, 0.35);
  }

  .live-dot {
    width: 10px;
    height: 10px;
    background-color: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 12px #34d399;
  }

  .live-text {
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.1em;
    color: #34d399;
    font-family: 'JetBrains Mono', monospace;
  }

  .countdown-hero {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 40px 0 20px 0;
  }

  .countdown-pill {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 12px 28px;
    background: rgba(99, 102, 241, 0.18);
    border: 1px solid rgba(129, 140, 248, 0.45);
    border-radius: 100px;
    margin-bottom: 24px;
  }

  .countdown-pill span {
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: #c7d2fe;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
  }

  .countdown-headline {
    font-size: 88px;
    line-height: 1.02;
    font-weight: 900;
    letter-spacing: -0.03em;
    text-transform: uppercase;
    margin-bottom: 20px;
  }

  .gradient-text-fire {
    background: linear-gradient(135deg, #ffffff 10%, #f1f5f9 40%, #38bdf8 70%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .gradient-text-accent {
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .teaser-quote {
    font-size: 32px;
    font-weight: 700;
    color: #e2e8f0;
    display: inline-flex;
    align-items: center;
    gap: 16px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 12px 32px;
    border-radius: 100px;
  }

  .teaser-quote .highlight { color: #38bdf8; font-weight: 800; }

  .pipeline-card {
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-radius: 28px;
    padding: 32px;
    backdrop-filter: blur(24px);
    margin: 20px 0;
  }

  .terminal-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 20px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 24px;
  }

  .window-dots { display: flex; gap: 8px; }
  .w-dot { width: 14px; height: 14px; border-radius: 50%; }
  .w-dot.red { background: #ef4444; }
  .w-dot.yellow { background: #f59e0b; }
  .w-dot.green { background: #10b981; }

  .terminal-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    color: #38bdf8;
    font-weight: 600;
  }

  .pipeline-steps-vertical {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 24px;
  }

  .p-step {
    display: flex;
    align-items: center;
    gap: 18px;
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 16px 20px;
    border-radius: 16px;
  }

  .p-step.success { border-color: rgba(52, 211, 153, 0.4); }

  .p-icon {
    width: 32px;
    height: 32px;
    background: #10b981;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .p-step-content {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .p-step-title {
    font-size: 16px;
    font-weight: 700;
    color: #ffffff;
  }

  .p-step-desc {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #94a3b8;
  }

  .console-strip {
    background: #090d16;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 14px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
  }

  .copywriting-box {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.04) 0%, rgba(255, 255, 255, 0.01) 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 28px 32px;
    margin-bottom: 20px;
  }

  .copy-headline {
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .copy-body {
    font-size: 16px;
    line-height: 1.6;
    color: #cbd5e1;
  }

  .copy-body strong { color: #f8fafc; }

  .poster-footer {
    display: flex;
    flex-direction: column;
    gap: 20px;
    background: rgba(11, 15, 25, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 24px;
    padding: 28px 32px;
    backdrop-filter: blur(20px);
  }

  .footer-row-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .date-block { display: flex; align-items: center; gap: 18px; }

  .date-calendar-icon {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #4f46e5, #06b6d4);
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .cal-month { font-size: 11px; font-weight: 800; color: #e0f2fe; }
  .cal-day { font-size: 26px; font-weight: 900; color: #ffffff; line-height: 1; }

  .date-main { font-size: 22px; font-weight: 800; color: #ffffff; }
  .date-sub { font-size: 14px; color: #94a3b8; }

  .portal-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(56, 189, 248, 0.15);
    border: 1px solid rgba(56, 189, 248, 0.4);
    padding: 12px 24px;
    border-radius: 100px;
  }

  .portal-pill span {
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    font-weight: 700;
    color: #38bdf8;
  }

  .footer-row-bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #64748b;
  }
</style>
</head>
<body>
  <div class="bg-glow-top"></div>
  <div class="bg-glow-bottom"></div>
  <div class="cyber-grid"></div>

  <div class="content-layer">
    <header class="poster-header">
      <div class="brand-group">
        <div class="brand-icon">
          <svg viewBox="0 0 24 24">
            <path d="M12 2.5s4 4 4 10.5c0 2.5-1.5 4.5-4 5.5-2.5-1-4-3-4-5.5 0-6.5 4-10.5 4-10.5z"/>
            <path d="M5 13c-2 2-2 5-2 5s3 0 5-2"/>
            <path d="M19 13c2 2 2 5 2 5s-3 0-5-2"/>
          </svg>
        </div>
        <div>
          <div class="brand-title">Proxsis Connect</div>
          <div class="brand-subtitle">Cloud PaaS • Powered by Coolify</div>
        </div>
      </div>
      <div class="live-pill">
        <div class="live-dot"></div>
        <div class="live-text">Live Demo Soon</div>
      </div>
    </header>

    <section class="countdown-hero">
      <div class="countdown-pill">
        <span>⏱️ Official Countdown</span>
      </div>
      <h1 class="countdown-headline">
        <span class="gradient-text-fire">TOMORROW,</span><br>
        <span class="gradient-text-accent">WE GO LIVE!</span>
      </h1>
      <div class="teaser-quote">
        <span>“See it <span class="highlight">built</span>. See it <span class="highlight">deployed</span>.”</span>
      </div>
    </section>

    <div class="pipeline-card">
      <div class="terminal-topbar">
        <div class="window-dots">
          <div class="w-dot red"></div>
          <div class="w-dot yellow"></div>
          <div class="w-dot green"></div>
        </div>
        <div class="terminal-title">connect.proxsis.com</div>
      </div>

      <div class="pipeline-steps-vertical">
        <div class="p-step success">
          <div class="p-icon">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <div class="p-step-content">
            <div class="p-step-title">01 • Source & Git Push</div>
            <div class="p-step-desc">Otomasi build container dari repositori GitHub & GitLab</div>
          </div>
        </div>

        <div class="p-step success">
          <div class="p-icon">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <div class="p-step-content">
            <div class="p-step-title">02 • Self-Hosted PaaS Engine</div>
            <div class="p-step-desc">Isolasi aman di server VM on-premise Proxmox Proxsis</div>
          </div>
        </div>

        <div class="p-step success">
          <div class="p-icon">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <div class="p-step-content">
            <div class="p-step-title">03 • Zero-Downtime Deployment</div>
            <div class="p-step-desc">Instant SSL, custom sub-domain & monitoring aktif</div>
          </div>
        </div>
      </div>

      <div class="console-strip">
        <div style="display: flex; gap: 8px;">
          <span style="color: #10b981;">$</span>
          <span>coolify deploy --all</span>
        </div>
        <div style="color: #34d399; font-weight: 700;">LIVE IN PRODUCTION ✓</div>
      </div>
    </div>

    <div class="copywriting-box">
      <div class="copy-headline">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="#38bdf8"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        <span>Live Demonstration Walkthrough</span>
      </div>
      <p class="copy-body">
        Besok, kita akan mengenal <strong>Proxsis Connect</strong> lebih dekat dan melihat langsung bagaimana aplikasi bisa di-deploy dari proses build sampai aplikasi siap diakses. <strong>Jangan lewatkan live demo-nya!</strong>
      </p>
    </div>

    <footer class="poster-footer">
      <div class="footer-row-top">
        <div class="date-block">
          <div class="date-calendar-icon">
            <span class="cal-month">NOV</span>
            <span class="cal-day">11</span>
          </div>
          <div class="date-details">
            <div class="date-main">Rabu, 11 November 2026</div>
            <div class="date-sub">Live Deployment Demo & Sosialisasi PaaS</div>
          </div>
        </div>

        <div class="portal-pill">
          <span>connect.proxsis.com</span>
        </div>
      </div>

      <div class="footer-row-bottom">
        <div>#ProxsisConnect #Coolify #LaunchDay</div>
        <div>Proxsis Infrastructure & AI Ecosystem</div>
      </div>
    </footer>
  </div>
</body>
</html>
"""

configs = [
    {
        "name": "feed_portrait_4x5",
        "html_file": os.path.join(OUTPUT_DIR, "poster_feed_portrait.html"),
        "png_file": os.path.join(OUTPUT_DIR, "poster_feed_portrait.png"),
        "width": 1080,
        "height": 1350,
        "content": html_portrait,
    },
    {
        "name": "feed_square_1x1",
        "html_file": os.path.join(OUTPUT_DIR, "poster_feed_square.html"),
        "png_file": os.path.join(OUTPUT_DIR, "poster_feed_square.png"),
        "width": 1080,
        "height": 1080,
        "content": html_square,
    },
    {
        "name": "story_vertical_9x16",
        "html_file": os.path.join(OUTPUT_DIR, "poster_story_vertical.html"),
        "png_file": os.path.join(OUTPUT_DIR, "poster_story_vertical.png"),
        "width": 1080,
        "height": 1920,
        "content": html_story,
    }
]

for cfg in configs:
    with open(cfg["html_file"], "w", encoding="utf-8") as f:
        f.write(cfg["content"])
    print(f"HTML written: {cfg['html_file']}")

    cmd = [
        "google-chrome",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=3500",
        f"--window-size={cfg['width']},{cfg['height']}",
        "--force-device-scale-factor=2",
        f"--screenshot={cfg['png_file']}",
        f"file://{cfg['html_file']}"
    ]

    print(f"Rendering {cfg['name']} screenshot with Chrome headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        file_sz = os.path.getsize(cfg['png_file'])
        print(f"✓ Rendered: {cfg['png_file']} ({file_sz} bytes)")
    else:
        print(f"✗ Failed rendering {cfg['name']}: {res.stderr}")

print("All posters generated successfully!")
