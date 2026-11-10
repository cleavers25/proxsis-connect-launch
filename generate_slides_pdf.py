import os
import subprocess
import sys

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Sosialisasi & Panduan Praktis Coolify — Proxsis Group</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

  @page {
    size: 1920px 1080px;
    margin: 0;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    background-color: #0b0f19;
    color: #f1f5f9;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .slide {
    width: 1920px;
    height: 1080px;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    break-after: page;
    background: radial-gradient(circle at 85% 15%, rgba(99, 102, 241, 0.12) 0%, transparent 45%),
                radial-gradient(circle at 15% 85%, rgba(14, 165, 233, 0.10) 0%, transparent 45%),
                #0b0f19;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* Slide specific backgrounds */
  .slide.cover {
    background: radial-gradient(circle at 50% 30%, rgba(99, 102, 241, 0.22) 0%, transparent 60%),
                radial-gradient(circle at 80% 80%, rgba(56, 189, 248, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 20% 70%, rgba(168, 85, 247, 0.15) 0%, transparent 50%),
                #070a12;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 80px 120px;
  }

  /* HEADER */
  .slide-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 24px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 18px;
  }

  .header-left {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .pill-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    padding: 6px 14px;
    border-radius: 9999px;
    background: rgba(99, 102, 241, 0.18);
    color: #a5b4fc;
    border: 1px solid rgba(99, 102, 241, 0.35);
    width: fit-content;
  }

  .pill-badge.cyan {
    background: rgba(14, 165, 233, 0.18);
    color: #7dd3fc;
    border-color: rgba(14, 165, 233, 0.35);
  }

  .pill-badge.emerald {
    background: rgba(16, 185, 129, 0.18);
    color: #6ee7b7;
    border-color: rgba(16, 185, 129, 0.35);
  }

  .pill-badge.amber {
    background: rgba(245, 158, 11, 0.18);
    color: #fcd34d;
    border-color: rgba(245, 158, 11, 0.35);
  }

  .slide-title {
    font-size: 38px;
    font-weight: 800;
    line-height: 1.2;
    background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .slide-subtitle {
    font-size: 18px;
    color: #94a3b8;
    font-weight: 500;
  }

  .header-tag {
    font-size: 13px;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    text-align: right;
  }

  /* FOOTER */
  .slide-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 16px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-size: 13px;
    color: #64748b;
    font-weight: 500;
  }

  .slide-footer .brand {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #94a3b8;
    font-weight: 600;
  }

  .slide-footer .brand span {
    color: #6366f1;
  }

  .slide-number {
    background: rgba(255, 255, 255, 0.05);
    padding: 4px 12px;
    border-radius: 6px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #cbd5e1;
    font-weight: 600;
  }

  /* CONTENT AREA */
  .slide-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 24px;
  }

  /* GRIDS */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 28px;
  }

  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 24px;
  }

  .grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 20px;
  }

  .grid-2-1 {
    display: grid;
    grid-template-columns: 1.6fr 1fr;
    gap: 28px;
  }

  .grid-1-2 {
    display: grid;
    grid-template-columns: 1fr 1.6fr;
    gap: 28px;
  }

  /* CARDS */
  .card {
    background: rgba(30, 41, 59, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 24px 28px;
    backdrop-filter: blur(10px);
    display: flex;
    flex-direction: column;
    gap: 12px;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
  }

  .card.highlight {
    border-color: rgba(99, 102, 241, 0.4);
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(30, 41, 59, 0.6) 100%);
  }

  .card.success {
    border-color: rgba(16, 185, 129, 0.4);
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(30, 41, 59, 0.6) 100%);
  }

  .card.warning {
    border-color: rgba(245, 158, 11, 0.4);
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(30, 41, 59, 0.6) 100%);
  }

  .card-title {
    font-size: 20px;
    font-weight: 700;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .card-desc {
    font-size: 15px;
    color: #94a3b8;
    line-height: 1.55;
  }

  /* LIST ITEMS */
  .list-stack {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .list-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 15px;
    color: #cbd5e1;
    line-height: 1.45;
  }

  .list-bullet {
    width: 22px;
    height: 22px;
    border-radius: 6px;
    background: rgba(99, 102, 241, 0.2);
    color: #818cf8;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 12px;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .list-bullet.emerald {
    background: rgba(16, 185, 129, 0.2);
    color: #34d399;
  }

  .list-bullet.cyan {
    background: rgba(14, 165, 233, 0.2);
    color: #38bdf8;
  }

  .list-bullet.amber {
    background: rgba(245, 158, 11, 0.2);
    color: #fbbf24;
  }

  .tag-pill {
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
  }
  .tag-good { background: rgba(16, 185, 129, 0.2); color: #34d399; }
  .tag-neutral { background: rgba(245, 158, 11, 0.2); color: #fbbf24; }
  .tag-bad { background: rgba(239, 68, 68, 0.2); color: #f87171; }

  /* CODE BOX */
  .code-block {
    background: #070a12;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    padding: 16px 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #38bdf8;
    line-height: 1.6;
    overflow: hidden;
  }

  .code-header {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }

  .dot { width: 10px; height: 10px; border-radius: 50%; }
  .dot.red { background: #ef4444; }
  .dot.yellow { background: #f59e0b; }
  .dot.green { background: #10b981; }

  /* STEP BOX */
  .step-container {
    display: flex;
    gap: 20px;
  }

  .step-card {
    flex: 1;
    background: rgba(30, 41, 59, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    position: relative;
  }

  .step-num {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
    color: white;
    font-weight: 800;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
  }

</style>
</head>
<body>

<!-- SLIDE 1: COVER -->
<div class="slide cover">
  <div style="display: flex; flex-direction: column; align-items: center; gap: 20px; max-width: 1200px;">
    <div style="display: flex; gap: 12px;">
      <span class="pill-badge emerald">PROXSIS GROUP • CLOUD & AI INFRA</span>
      <span class="pill-badge cyan">INTERNAL WORKSHOP & SOCIALIZATION</span>
    </div>
    
    <div style="font-size: 64px; font-weight: 800; line-height: 1.15; letter-spacing: -1px;">
      SOSIALISASI & PANDUAN LENGKAP<br>
      <span style="background: linear-gradient(135deg, #818cf8 0%, #38bdf8 50%, #34d399 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        COOLIFY PAAS & DEPLOYMENT AI
      </span>
    </div>

    <p style="font-size: 22px; color: #94a3b8; line-height: 1.6; max-width: 950px; font-weight: 400;">
      Modern Self-Hosted PaaS untuk Ekosistem Aplikasi Proxsis: Efisiensi Biaya, Akses User & Role, Otomasi AI Agent, serta Standar Operasional & Maintenance Tim Infra.
    </p>

    <div style="display: flex; gap: 32px; margin-top: 36px; padding: 18px 36px; background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px;">
      <div style="text-align: left;">
        <div style="font-size: 12px; color: #64748b; text-transform: uppercase; font-weight: 700;">Host URL</div>
        <div style="font-size: 16px; color: #38bdf8; font-family: 'JetBrains Mono', monospace; font-weight: 600;">https://connect.proxsis.com</div>
      </div>
      <div style="width: 1px; background: rgba(255, 255, 255, 0.1);"></div>
      <div style="text-align: left;">
        <div style="font-size: 12px; color: #64748b; text-transform: uppercase; font-weight: 700;">Cluster Node</div>
        <div style="font-size: 16px; color: #f8fafc; font-weight: 600;">Sitkrop Infra (Proxmox 192.168.10.21)</div>
      </div>
      <div style="width: 1px; background: rgba(255, 255, 255, 0.1);"></div>
      <div style="text-align: left;">
        <div style="font-size: 12px; color: #64748b; text-transform: uppercase; font-weight: 700;">Official AI Agent</div>
        <div style="font-size: 16px; color: #a5b4fc; font-weight: 600;">Google Antigravity & Claude Code</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 2: AGENDA & 4 PILAR UTAMA -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge">STRUKTUR PEMBAHASAN</span>
      <h1 class="slide-title">Agenda & 4 Pilar Sosialisasi</h1>
      <p class="slide-subtitle">Ikhtisar materi dari pengenalan fundamental hingga operasional mendalam</p>
    </div>
    <div class="header-tag">Overview Agenda</div>
  </div>

  <div class="slide-body">
    <div class="grid-4">
      <div class="card highlight">
        <div class="step-num" style="background: linear-gradient(135deg, #6366f1 0%, #4338ca 100%);">01</div>
        <div class="card-title" style="font-size: 22px;">Latar Belakang & Fitur Coolify</div>
        <div class="card-desc">
          Tantangan deployment lama, kedaulatan data on-premise, keunggulan PaaS mandiri, dan fitur inti Coolify.
        </div>
        <div style="margin-top: auto; font-size: 13px; color: #a5b4fc; font-weight: 600;">
          → Slide 03 - 04
        </div>
      </div>

      <div class="card">
        <div class="step-num" style="background: linear-gradient(135deg, #0ea5e9 0%, #0369a1 100%);">02</div>
        <div class="card-title" style="font-size: 22px;">Manajemen Akun & Login</div>
        <div class="card-desc">
          Alur registrasi akun developer, hierarki Team & Project, setup hak akses role-based (RBAC), serta pembuatan API Token.
        </div>
        <div style="margin-top: auto; font-size: 13px; color: #7dd3fc; font-weight: 600;">
          → Slide 05 - 06
        </div>
      </div>

      <div class="card success">
        <div class="step-num" style="background: linear-gradient(135deg, #10b981 0%, #047857 100%);">03</div>
        <div class="card-title" style="font-size: 22px;">Deploy Aplikasi via AI Agent</div>
        <div class="card-desc">
          Standarisasi Agent (Antigravity & Claude Code), integrasi Git repository, auto-routing wildcard subdomain, dan workflow praktis.
        </div>
        <div style="margin-top: auto; font-size: 13px; color: #6ee7b7; font-weight: 600;">
          → Slide 07 - 09
        </div>
      </div>

      <div class="card warning">
        <div class="step-num" style="background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%);">04</div>
        <div class="card-title" style="font-size: 22px;">Maintenance Tim Infra (SOP)</div>
        <div class="card-desc">
          Prosedur rutin pembersihan docker cache, auto-backup database, update versi core, SSL management, dan disaster recovery runbook.
        </div>
        <div style="margin-top: auto; font-size: 13px; color: #fcd34d; font-weight: 600;">
          → Slide 10 - 12
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Sosialisasi Platform Coolify • Agenda</div>
    <div class="slide-number">02 / 13</div>
  </div>
</div>

<!-- SLIDE 3: LATAR BELAKANG & PROBLEM STATEMENT -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge">PILAR 1 • BACKGROUND</span>
      <h1 class="slide-title">Latar Belakang: Tantangan Deployment Tradisional</h1>
      <p class="slide-subtitle">Problem nyata di lapangan dan urgensi standardisasi PaaS internal Proxsis</p>
    </div>
    <div class="header-tag">Problem Statement</div>
  </div>

  <div class="slide-body">
    <div class="grid-2">
      <div class="card" style="border-left: 4px solid #ef4444;">
        <div class="card-title" style="color: #f87171;">
          ⚠️ Kendala Sebelum Ada Coolify
        </div>
        <div class="list-stack">
          <div class="list-item">
            <div class="list-bullet" style="background: rgba(239, 68, 68, 0.2); color: #f87171;">✕</div>
            <div>
              <strong style="color: #ffffff;">Setup Manual & Memakan Waktu:</strong> Developer dan konsultan harus request konfigurasi Nginx/Caddyfile, firewall port, dan SSL setiap kali ingin showcase prototype/aplikasi baru.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet" style="background: rgba(239, 68, 68, 0.2); color: #f87171;">✕</div>
            <div>
              <strong style="color: #ffffff;">Biaya Cloud SaaS Membengkak:</strong> Layanan seperti Heroku ($7-$25/app/bln) atau Render/AWS cepat menjadi tidak efisien saat jumlah aplikasi pengujian dan microservices bertambah puluhan.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet" style="background: rgba(239, 68, 68, 0.2); color: #f87171;">✕</div>
            <div>
              <strong style="color: #ffffff;">Resiko Keamanan & SSH Sprawl:</strong> Membagikan akses SSH VPS langsung ke banyak orang rawan salah ketik, bentrok port aplikasi, hingga insiden kebocoran server.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet" style="background: rgba(239, 68, 68, 0.2); color: #f87171;">✕</div>
            <div>
              <strong style="color: #ffffff;">AI Agent Terisolasi:</strong> Tool AI modern (Antigravity, Cursor) kesulitan melakukan deploy jika proses infrastruktur tidak memiliki REST API yang terstandar.
            </div>
          </div>
        </div>
      </div>

      <div class="card success" style="border-left: 4px solid #10b981;">
        <div class="card-title" style="color: #34d399;">
          🎯 Solusi & Target yang Dicapai Bersama Coolify
        </div>
        <div class="list-stack">
          <div class="list-item">
            <div class="list-bullet emerald">✓</div>
            <div>
              <strong style="color: #ffffff;">Zero-Config Developer Experience:</strong> Push kode ke Git, aplikasi langsung live dengan HTTPS domain tanpa perlu intervensi manual tim infra.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet emerald">✓</div>
            <div>
              <strong style="color: #ffffff;">Efisiensi Finansial (Self-Hosted on Proxmox):</strong> Memanfaatkan server VM on-premise Proxsis yang ada (Sitkrop Infra 192.168.10.21) tanpa biaya langganan bulanan per aplikasi.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet emerald">✓</div>
            <div>
              <strong style="color: #ffffff;">Kedaulatan Data & Keamanan Penuh:</strong> Seluruh database dan source code tetap berada di jaringan internal Proxsis dengan isolasi container Docker & RBAC.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet emerald">✓</div>
            <div>
              <strong style="color: #ffffff;">100% AI-Agent Ready:</strong> Terintegrasi sempurna dengan REST API Coolify, memungkinkan AI Agent men-deploy proyek dalam 1 baris prompt chat!
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Latar Belakang & Kebutuhan PaaS</div>
    <div class="slide-number">03 / 13</div>
  </div>
</div>

<!-- SLIDE 4: FITUR & FUNGSI UTAMA COOLIFY -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge emerald">PILAR 1 • FITUR INTI</span>
      <h1 class="slide-title">Fungsi Utama Coolify untuk Kebutuhan Organisasi</h1>
      <p class="slide-subtitle">Solusi all-in-one untuk hosting aplikasi, database, dan layanan pendukung</p>
    </div>
    <div class="header-tag">Core Features</div>
  </div>

  <div class="slide-body">
    <div class="grid-3">
      <div class="card">
        <div style="font-size: 32px;">🚀</div>
        <div class="card-title">Multi-Framework Runtime</div>
        <div class="card-desc">
          Mendukung berbagai bahasa pemrograman tanpa perlu membuat Dockerfile manual berkat <strong>Nixpacks</strong> & <strong>Buildpacks</strong>:
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px;">
          <span class="tag-pill tag-good">Node.js / React</span>
          <span class="tag-pill tag-good">Next.js / Vue</span>
          <span class="tag-pill tag-good">Python / FastAPI</span>
          <span class="tag-pill tag-good">PHP / Laravel</span>
          <span class="tag-pill tag-good">Go / Rust</span>
          <span class="tag-pill tag-good">Static HTML</span>
        </div>
      </div>

      <div class="card">
        <div style="font-size: 32px;">🗄️</div>
        <div class="card-title">Instant Managed Databases</div>
        <div class="card-desc">
          Deploy database production-ready dalam 10 detik dengan persistence storage dan antarmuka manajemen:
        </div>
        <div class="list-stack" style="gap: 8px; margin-top: 8px;">
          <div class="list-item"><div class="list-bullet cyan">✓</div><div>PostgreSQL, MySQL, MariaDB</div></div>
          <div class="list-item"><div class="list-bullet cyan">✓</div><div>Redis Cache & KeyDB</div></div>
          <div class="list-item"><div class="list-bullet cyan">✓</div><div>MinIO (S3-compatible Object Storage)</div></div>
          <div class="list-item"><div class="list-bullet cyan">✓</div><div>Jadwal Automated Snapshot harian</div></div>
        </div>
      </div>

      <div class="card">
        <div style="font-size: 32px;">🛡️</div>
        <div class="card-title">Auto-SSL & Reverse Proxy</div>
        <div class="card-desc">
          Terintegrasi langsung dengan Traefik Proxy bawaan:
        </div>
        <div class="list-stack" style="gap: 8px; margin-top: 8px;">
          <div class="list-item"><div class="list-bullet emerald">✓</div><div>Sertifikat SSL Let's Encrypt otomatis</div></div>
          <div class="list-item"><div class="list-bullet emerald">✓</div><div>Zero-downtime rolling deployment</div></div>
          <div class="list-item"><div class="list-bullet emerald">✓</div><div>Domain wildcard auto-routing</div></div>
          <div class="list-item"><div class="list-bullet emerald">✓</div><div>Health check & auto-restart container</div></div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Fitur & Fungsi Utama Coolify</div>
    <div class="slide-number">04 / 13</div>
  </div>
</div>

<!-- SLIDE 5: CARA BUAT AKUN & LOGIN -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge cyan">PILAR 2 • ONBOARDING USER</span>
      <h1 class="slide-title">Cara Buat Akun & Login di Coolify</h1>
      <p class="slide-subtitle">Panduan langkah demi langkah akses portal untuk anggota tim baru</p>
    </div>
    <div class="header-tag">Authentication & Onboarding</div>
  </div>

  <div class="slide-body">
    <div class="step-container">
      <div class="step-card">
        <div class="step-num">1</div>
        <div class="card-title" style="font-size: 18px;">Buka Portal Resmi</div>
        <div class="card-desc">
          Akses portal Coolify Proxsis melalui browser di URL:
        </div>
        <div class="code-block" style="color: #38bdf8; font-weight: 600; text-align: center; padding: 10px;">
          https://connect.proxsis.com
        </div>
        <div class="card-desc" style="font-size: 13px;">
          Gunakan koneksi internet biasa (sudah diproteksi SSL Cloudflare).
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">2</div>
        <div class="card-title" style="font-size: 18px;">Registrasi / Undangan</div>
        <div class="card-desc">
          Pilih salah satu metode registrasi yang berlaku:
        </div>
        <div class="list-stack" style="gap: 8px;">
          <div class="list-item" style="font-size: 13px;">
            <div class="list-bullet cyan">•</div>
            <div><strong>Undangan Email:</strong> Cek inbox email kerja (@proxsis.com / @proxsisgroup.com) dari Tim Infra lalu klik link aktivasi.</div>
          </div>
          <div class="list-item" style="font-size: 13px;">
            <div class="list-bullet cyan">•</div>
            <div><strong>Direct Register:</strong> Klik <em>"Register"</em> jika self-registration aktif, masukkan Nama, Email kerja, dan Password kuat.</div>
          </div>
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">3</div>
        <div class="card-title" style="font-size: 18px;">Login & Masuk Dashboard</div>
        <div class="card-desc">
          Masukkan kredensial yang telah didaftarkan:
        </div>
        <div class="list-stack" style="gap: 8px;">
          <div class="list-item" style="font-size: 13px;">
            <div class="list-bullet emerald">•</div>
            <div>Klik <strong>Login</strong> untuk masuk ke workspace Coolify.</div>
          </div>
          <div class="list-item" style="font-size: 13px;">
            <div class="list-bullet emerald">•</div>
            <div>Pilih <strong>Team / Workspace</strong> divisi Anda di pojok kiri atas (misal: <em>Biztech, Infra, R&D</em>).</div>
          </div>
        </div>
      </div>

      <div class="step-card">
        <div class="step-num">4</div>
        <div class="card-title" style="font-size: 18px;">Verifikasi Role (RBAC)</div>
        <div class="card-desc">
          Pastikan role Anda sesuai tugas:
        </div>
        <div class="list-stack" style="gap: 6px; font-size: 13px;">
          <div><span class="tag-pill tag-good">Developer</span> Deploy & kelola app sendiri</div>
          <div><span class="tag-pill tag-neutral">Viewer</span> Hanya pantau logs & metrics</div>
          <div><span class="tag-pill tag-bad">Admin</span> Khusus Tim Infra / Lead</div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Registrasi & Login Akun Coolify</div>
    <div class="slide-number">05 / 13</div>
  </div>
</div>

<!-- SLIDE 6: GENERATE API TOKEN COOLIFY -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge cyan">PILAR 2 • KREDENSIAL API</span>
      <h1 class="slide-title">Cara Membuat API Token untuk AI Agent</h1>
      <p class="slide-subtitle">Kunci otentikasi agar Google Antigravity & Claude Code dapat mengotomasi deployment</p>
    </div>
    <div class="header-tag">API Token Generation</div>
  </div>

  <div class="slide-body">
    <div class="grid-2-1">
      <div class="card">
        <div class="card-title">Tahapan Pembuatan Token di Dashboard</div>
        <div class="list-stack">
          <div class="list-item">
            <div class="list-bullet">1</div>
            <div>
              <strong>Buka Menu Profile:</strong> Klik avatar / foto profil Anda di pojok kanan atas, lalu pilih menu <strong>Settings</strong> atau <strong>API Tokens</strong> (<code>/security/api-tokens</code>).
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet">2</div>
            <div>
              <strong>Klik Create New Token:</strong> Beri nama token yang deskriptif, contoh: <code>ai-deployment-antigravity</code> atau <code>laptop-fahima-agent</code>.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet">3</div>
            <div>
              <strong>Copy & Simpan Token:</strong> Salin string token yang muncul (token hanya ditampilkan <strong>satu kali</strong>). Simpan di credential manager atau file konfigurasi lokal Anda.
            </div>
          </div>
        </div>

        <div style="margin-top: 12px; padding: 14px 18px; background: rgba(99, 102, 241, 0.1); border-radius: 10px; border-left: 3px solid #6366f1;">
          <div style="font-size: 14px; color: #cbd5e1;">
            💡 <strong>Prinsip Least-Privilege:</strong> Buat token terpisah untuk tiap AI tool atau anggota tim. Jangan membagikan token admin utama ke channel publik!
          </div>
        </div>
      </div>

      <div class="card highlight">
        <div class="card-title" style="font-size: 18px;">Penyimpanan di Konfigurasi AI</div>
        <div class="card-desc">
          Paste token Anda ke dalam file konfigurasi <code>AI_DEPLOYMENT_CONFIG.md</code>:
        </div>
        <div class="code-block" style="font-size: 12px;">
          <div class="code-header">
            <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
            <span style="color: #64748b; margin-left: 6px;">AI_DEPLOYMENT_CONFIG.md</span>
          </div>
          <span style="color: #64748b;"># 1. GitHub Token Personal</span><br>
          <span style="color: #f43f5e;">GITHUB_TOKEN</span>=<span style="color: #34d399;">"ghp_xxxx..."</span><br><br>
          <span style="color: #64748b;"># 2. Coolify API Token</span><br>
          <span style="color: #f43f5e;">COOLIFY_TOKEN</span>=<span style="color: #34d399;">"1|abcdef..."</span><br><br>
          <span style="color: #64748b;"># 3. URL Repo (Opsional)</span><br>
          <span style="color: #f43f5e;">GIT_REPOSITORY</span>=<span style="color: #34d399;">""</span>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Pembuatan & Manajemen API Token</div>
    <div class="slide-number">06 / 13</div>
  </div>
</div>

<!-- SLIDE 7: STANDARISASI TOOL AI AGENT -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge emerald">PILAR 3 • STANDARISASI AI</span>
      <h1 class="slide-title">Standarisasi AI Agent: Pilihan Tool & Tiering Support</h1>
      <p class="slide-subtitle">Pelajaran dari kasus lapangan dan penentuan platform AI resmi internal Proxsis</p>
    </div>
    <div class="header-tag">AI Agent Governance</div>
  </div>

  <div class="slide-body">
    <div class="grid-3">
      <div class="card highlight">
        <div class="card-title">
          <span class="tag-pill tag-good">Tier 1 • Utama</span>
          Google Antigravity
        </div>
        <div class="card-desc">
          <strong>FULL SUPPORT ⭐</strong><br>
          Standar default internal Proxsis. Zero-config, eksekusi shell native, error self-healing, dan integrasi penuh dengan filesystem lokal.
        </div>
      </div>

      <div class="card highlight">
        <div class="card-title">
          <span class="tag-pill tag-good">Tier 1 • Utama</span>
          Claude Code (CLI)
        </div>
        <div class="card-desc">
          <strong>FULL SUPPORT</strong><br>
          Alternatif resmi bagi user dengan langganan Claude Pro/Team. Dijalankan via terminal (<code>claude</code>) dengan kapabilitas eksekusi bash setara.
        </div>
      </div>

      <div class="card">
        <div class="card-title">
          <span class="tag-pill tag-good">Tier 1 • Developer</span>
          VS Code + Kilo / Cline
        </div>
        <div class="card-desc">
          <strong>FULL SUPPORT</strong><br>
          Khusus engineer yang membutuhkan kontrol kode mendalam langsung di IDE, dengan terminal execution terintegrasi.
        </div>
      </div>
    </div>

    <div style="padding: 18px 24px; background: rgba(245, 158, 11, 0.1); border-radius: 12px; border-left: 4px solid #f59e0b; display: flex; align-items: center; gap: 16px;">
      <span style="font-size: 28px;">💡</span>
      <div style="font-size: 15px; color: #cbd5e1; line-height: 1.5;">
        <strong>Kebijakan Resmi Tim Infra untuk Pengguna Claude:</strong><br>
        Claude Desktop GUI polosan <em>tidak didukung</em> untuk otomasi deployment karena terisolasi tanpa akses terminal. Seluruh pengguna Claude cukup diarahkan menginstal <strong>Claude Code CLI</strong> (<code>npm i -g @anthropic-ai/claude-code</code>) menggunakan akun Claude yang sama.
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Standarisasi & Matriks Dukungan AI Agent</div>
    <div class="slide-number">07 / 13</div>
  </div>
</div>

<!-- SLIDE 8: ALUR DEPLOY DENGAN AI STEP BY STEP -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge emerald">PILAR 3 • PRAKTEK DEPLOY</span>
      <h1 class="slide-title">Cara Deploy Aplikasi dengan AI: Alur Kerja Nyata</h1>
      <p class="slide-subtitle">Bagaimana AI mengeksekusi end-to-end deployment hanya dengan 1 instruksi chat</p>
    </div>
    <div class="header-tag">AI Deployment Workflow</div>
  </div>

  <div class="slide-body">
    <div class="grid-2">
      <div class="card highlight">
        <div class="card-title">
          <span>💬</span> 1. Prompt Sederhana Pengguna
        </div>
        <div class="card-desc">
          User (Developer/PM) cukup membuka Google Antigravity / Claude Code di folder proyeknya dan mengetik:
        </div>
        <div class="code-block" style="color: #f8fafc; font-size: 14px; border-color: rgba(99, 102, 241, 0.4);">
          <span style="color: #818cf8;">User ></span> "Tolong deploy aplikasi landing page ini ke Coolify dengan domain biztech-fahima-portal.connect.proxsis.com"
        </div>

        <div class="card-title" style="margin-top: 14px;">
          <span>🤖</span> 2. Eksekusi Otomatis AI Agent
        </div>
        <div class="list-stack">
          <div class="list-item">
            <div class="list-bullet emerald">A</div>
            <div><strong>Baca Konfigurasi:</strong> AI membaca token dari <code>AI_DEPLOYMENT_CONFIG.md</code>.</div>
          </div>
          <div class="list-item">
            <div class="list-bullet emerald">B</div>
            <div><strong>Git Sync:</strong> Melakukan git commit dan push repository ke GitHub.</div>
          </div>
          <div class="list-item">
            <div class="list-bullet emerald">C</div>
            <div><strong>API Registration:</strong> Mendaftarkan aplikasi ke server <em>Sitkrop Infra</em> via Coolify REST API.</div>
          </div>
          <div class="list-item">
            <div class="list-bullet emerald">D</div>
            <div><strong>Domain Binding:</strong> Memasang domain wildcard dan mentrigger proses build & live.</div>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-title">
          <span>⚡</span> Output & Hasil Instan di Terminal
        </div>
        <div class="code-block" style="font-size: 12px; color: #a5b4fc;">
          <div class="code-header">
            <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
            <span style="color: #64748b; margin-left: 6px;">terminal-log (antigravity execution)</span>
          </div>
          <span style="color: #10b981;">✔ Project UUID :</span> cl89x8... (Web Projects)<br>
          <span style="color: #10b981;">✔ Server Target:</span> Sitkrop Infra (192.168.10.21)<br>
          <span style="color: #10b981;">✔ GitHub Repo  :</span> https://github.com/cleavers25/portal<br>
          <span style="color: #10b981;">✔ App Created  :</span> uuid=d4x9p02a11b8...<br>
          <span style="color: #10b981;">✔ Domain Set   :</span> https://biztech-fahima-portal.connect.proxsis.com<br>
          <span style="color: #f59e0b;">⏳ Status Build :</span> Pulling Nixpacks & Building container...<br>
          <span style="color: #34d399; font-weight: 700;">🚀 SUCCESS: Aplikasi LIVE & HTTPS Aktif!</span>
        </div>

        <div style="margin-top: 10px; padding: 12px; background: rgba(16, 185, 129, 0.1); border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.3);">
          <div style="font-size: 13px; color: #e2e8f0;">
            <strong>Waktu Eksekusi:</strong> Hanya ~90 detik dari pengetikan prompt hingga URL bisa dibuka seluruh dunia!
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Alur Deployment Praktis via AI Agent</div>
    <div class="slide-number">08 / 13</div>
  </div>
</div>

<!-- SLIDE 9: GUARDRAILS & STANDARISASI SUBDOMAIN -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge warning">PILAR 3 • GUARDRAILS</span>
      <h1 class="slide-title">Standarisasi Subdomain & Guardrails Multi-Tenancy</h1>
      <p class="slide-subtitle">Mencegah tabrakan nama domain, server crash, dan kebocoran resource</p>
    </div>
    <div class="header-tag">Governance & Best Practices</div>
  </div>

  <div class="slide-body">
    <div class="grid-3">
      <div class="card warning">
        <div style="font-size: 28px;">🏷️</div>
        <div class="card-title">Standar Format Subdomain</div>
        <div class="card-desc">
          Untuk mencegah <em>Domain Collision</em> (tabrakan nama URL antar tim):
        </div>
        <div class="code-block" style="font-size: 11px; margin-top: 8px;">
          https://[divisi]-[user]-[project]<br>.connect.proxsis.com
        </div>
        <div style="font-size: 13px; color: #cbd5e1; margin-top: 8px;">
          <strong>Contoh Valid:</strong><br>
          • <code>biztech-fahima-status.connect.proxsis.com</code><br>
          • <code>infra-ulul-mon.connect.proxsis.com</code>
        </div>
      </div>

      <div class="card">
        <div style="font-size: 28px;">🎚️</div>
        <div class="card-title">Resource Limit per App</div>
        <div class="card-desc">
          Mencegah 1 container menguras habis RAM & CPU Proxmox VM:
        </div>
        <div class="list-stack" style="gap: 8px; margin-top: 8px; font-size: 13px;">
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>Sandbox Default:</strong> Max 512 MB RAM & 0.5 CPU Core.</div></div>
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>Internal Tools:</strong> Max 1 GB RAM & 1.0 CPU Core.</div></div>
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>Production App:</strong> Request khusus ke Tim Infra.</div></div>
        </div>
      </div>

      <div class="card">
        <div style="font-size: 28px;">🧹</div>
        <div class="card-title">Isolasi Lingkungan Project</div>
        <div class="card-desc">
          Pemisahan ketat project space pada dashboard Coolify:
        </div>
        <div class="list-stack" style="gap: 8px; margin-top: 8px; font-size: 13px;">
          <div class="list-item"><div class="list-bullet cyan">•</div><div><strong>Sandbox / R&D:</strong> Tempat coba-coba AI agent & prototype (Auto-cleanup aktif).</div></div>
          <div class="list-item"><div class="list-bullet cyan">•</div><div><strong>Staging & Production:</strong> Khusus rilis resmi, hak akses terbatas hanya Lead Dev/Infra.</div></div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Tata Kelola & Guardrails Multi-Tenancy</div>
    <div class="slide-number">09 / 13</div>
  </div>
</div>

<!-- SLIDE 10: MAINTENANCE RUTIN TIM INFRA -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge amber">PILAR 4 • INFRA RUNBOOK</span>
      <h1 class="slide-title">Maintenance Tim Infra: Rutinitas Harian & Mingguan</h1>
      <p class="slide-subtitle">SOP pemeliharaan server Sitkrop Infra (192.168.10.21) agar performa tetap prima</p>
    </div>
    <div class="header-tag">Infra Maintenance SOP</div>
  </div>

  <div class="slide-body">
    <div class="grid-3">
      <div class="card highlight">
        <div class="card-title" style="font-size: 18px;">
          <span>🧹</span> 1. Docker Garbage Collection
        </div>
        <div class="card-desc">
          Build container berulang dari AI dapat menghabiskan puluhan GB disk cache jika tidak dibersihkan berkala.
        </div>
        <div class="code-block" style="font-size: 11px;">
          <span style="color: #64748b;"># Cron job harian di node 192.168.10.21</span><br>
          0 3 * * * docker image prune -af --filter "until=72h"<br>
          0 4 * * 0 docker builder prune -af --keep-storage 5GB
        </div>
        <div style="font-size: 12px; color: #a5b4fc;">
          Menghapus image gantung & builder cache tanpa mematikan container aktif.
        </div>
      </div>

      <div class="card">
        <div class="card-title" style="font-size: 18px;">
          <span>💾</span> 2. Automated DB & State Backup
        </div>
        <div class="card-desc">
          Cadangkan database internal Coolify dan seluruh persistent volume project:
        </div>
        <div class="list-stack" style="gap: 8px; font-size: 13px;">
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>Data Direktori:</strong> <code>/data/coolify/</code> wajib di-snapshot setiap 24 jam.</div></div>
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>DB Backup:</strong> Dump database SQLite/PostgreSQL internal ke remote backup/S3.</div></div>
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>Retention:</strong> Simpan snapshot 7 hari terakhir.</div></div>
        </div>
      </div>

      <div class="card">
        <div class="card-title" style="font-size: 18px;">
          <span>📊</span> 3. Health & Resource Monitoring
        </div>
        <div class="card-desc">
          Inspeksi metrik vital server VM Proxmox secara rutin:
        </div>
        <div class="list-stack" style="gap: 8px; font-size: 13px;">
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>Disk Usage Alert:</strong> Pastikan utilisasi disk <code>/</code> di bawah 80%.</div></div>
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>Memory Pressure:</strong> Cek container zombie dengan <code>docker stats</code>.</div></div>
          <div class="list-item"><div class="list-bullet amber">•</div><div><strong>Traefik Logs:</strong> Pantau error 502/504 di logs proxy Coolify.</div></div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>SOP Maintenance Rutin Tim Infra</div>
    <div class="slide-number">10 / 13</div>
  </div>
</div>

<!-- SLIDE 11: UPDATE CORE & SSL MANAGEMENT -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge amber">PILAR 4 • SISTEM OPERASIONAL</span>
      <h1 class="slide-title">Maintenance Tim Infra: Update Versi, SSL & Keamanan</h1>
      <p class="slide-subtitle">Prosedur resmi pembaruan engine Coolify dan pemeliharaan sertifikat SSL</p>
    </div>
    <div class="header-tag">Upgrades & Security</div>
  </div>

  <div class="slide-body">
    <div class="grid-2">
      <div class="card">
        <div class="card-title">
          <span>🔄</span> Prosedur Aman Upgrade Versi Coolify
        </div>
        <div class="card-desc">
          Coolify merilis update fitur dan security patch setiap minggu. Ikuti runbook berikut:
        </div>
        <div class="list-stack" style="font-size: 14px;">
          <div class="list-item">
            <div class="list-bullet">1</div>
            <div><strong>Pre-Check:</strong> Cek release notes di GitHub Coolify dan pastikan backup <code>/data/coolify</code> sudah berhasil hari ini.</div>
          </div>
          <div class="list-item">
            <div class="list-bullet">2</div>
            <div><strong>One-Line Upgrade:</strong> Eksekusi installer resmi di server host:
              <div class="code-block" style="margin-top: 6px; font-size: 12px;">
                curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
              </div>
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet">3</div>
            <div><strong>Post-Check:</strong> Verifikasi semua container running:
              <div class="code-block" style="margin-top: 6px; font-size: 12px;">
                docker ps | grep coolify
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="card highlight">
        <div class="card-title">
          <span>🛡️</span> SSL, Traefik & Cloudflare WAF Handling
        </div>
        <div class="card-desc">
          Memastikan rantai lalu lintas domain tetap lancar tanpa kendala blokir:
        </div>
        <div class="list-stack" style="font-size: 14px;">
          <div class="list-item">
            <div class="list-bullet cyan">✓</div>
            <div>
              <strong>Traefik Cert Renewal:</strong> Coolify otomatis memperbarui sertifikat Let's Encrypt 30 hari sebelum masa kedaluwarsa.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet cyan">✓</div>
            <div>
              <strong>Cloudflare WAF Bypass:</strong> Request API dari script lokal/curl wajib menyertakan <code>-H "User-Agent: curl/8.5.0"</code> agar tidak terblokir HTTP 403 oleh bot-fight Cloudflare.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet cyan">✓</div>
            <div>
              <strong>Caddy Gateway Synchronization:</strong> Pastikan IP Sitkrop Infra (192.168.10.21) tetap statis di DHCP/Proxmox bridge.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Update Versi, SSL & Manajemen Keamanan</div>
    <div class="slide-number">11 / 13</div>
  </div>
</div>

<!-- SLIDE 12: DISASTER RECOVERY & TROUBLESHOOTING -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge amber">PILAR 4 • INCIDENT RESPONSE</span>
      <h1 class="slide-title">Disaster Recovery & Troubleshooting Runbook</h1>
      <p class="slide-subtitle">Panduan cepat penanganan insiden darurat bagi On-Call Engineer Tim Infra</p>
    </div>
    <div class="header-tag">Disaster Recovery Runbook</div>
  </div>

  <div class="slide-body">
    <div class="grid-3">
      <div class="card" style="border-left: 4px solid #ef4444;">
        <div class="card-title" style="color: #f87171; font-size: 18px;">
          🚨 Insiden: 502 / Bad Gateway
        </div>
        <div class="card-desc" style="font-size: 13px;">
          <strong>Penyebab:</strong> Container aplikasi crash, port internal salah, atau Traefik kehilangan mapping routing.
        </div>
        <div class="code-block" style="font-size: 11px;">
          <span style="color: #64748b;"># 1. Cek logs container app</span><br>
          docker logs --tail 100 &lt;container_id&gt;<br><br>
          <span style="color: #64748b;"># 2. Restart Traefik Proxy</span><br>
          docker restart coolify-proxy
        </div>
        <div style="font-size: 12px; color: #94a3b8;">
          Periksa apakah <code>ports_exposes</code> sesuai dengan port listen aplikasi (misal 3000 atau 80).
        </div>
      </div>

      <div class="card" style="border-left: 4px solid #f59e0b;">
        <div class="card-title" style="color: #fbbf24; font-size: 18px;">
          🚨 Insiden: Disk Penuh 100%
        </div>
        <div class="card-desc" style="font-size: 13px;">
          <strong>Penyebab:</strong> Build cache Nixpacks menumpuk saat banyak user mencoba deploy bersamaan.
        </div>
        <div class="code-block" style="font-size: 11px;">
          <span style="color: #64748b;"># Pembersihan darurat (Safe):</span><br>
          docker builder prune -af<br>
          docker image prune -af<br>
          journalctl --vacuum-time=2d
        </div>
        <div style="font-size: 12px; color: #94a3b8;">
          Jangan gunakan flag <code>-v</code> tanpa analisa karena bisa menghapus database volume aplikasi.
        </div>
      </div>

      <div class="card" style="border-left: 4px solid #a855f7;">
        <div class="card-title" style="color: #c084fc; font-size: 18px;">
          🚨 Insiden: Coolify Hang / Mati
        </div>
        <div class="card-desc" style="font-size: 13px;">
          <strong>Penyebab:</strong> Core Coolify service mengalami deadlock atau out of memory.
        </div>
        <div class="code-block" style="font-size: 11px;">
          <span style="color: #64748b;"># Restart seluruh stack Coolify:</span><br>
          cd /data/coolify/source<br>
          docker compose down<br>
          docker compose up -d
        </div>
        <div style="font-size: 12px; color: #94a3b8;">
          Aplikasi user lain tetap berjalan normal karena Traefik dan container user terisolasi.
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Troubleshooting Runbook & Incident Response</div>
    <div class="slide-number">12 / 13</div>
  </div>
</div>

<!-- SLIDE 13: KESIMPULAN & NEXT STEPS -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <span class="pill-badge emerald">PENUTUP & ROADMAP</span>
      <h1 class="slide-title">Kesimpulan, Roadmap & Langkah Selanjutnya</h1>
      <p class="slide-subtitle">Transformasi budaya deployment mandiri, aman, dan cerdas di Proxsis Group</p>
    </div>
    <div class="header-tag">Summary & Next Steps</div>
  </div>

  <div class="slide-body">
    <div class="grid-2">
      <div class="card success">
        <div class="card-title" style="color: #34d399;">
          🎯 Manfaat Nyata untuk Seluruh Tim
        </div>
        <div class="list-stack">
          <div class="list-item">
            <div class="list-bullet emerald">1</div>
            <div>
              <strong style="color: #ffffff;">Untuk Developer & Product Team:</strong> Siklus rilis prototipe jauh lebih cepat dari hari menjadi hitungan menit via AI Agent tanpa hambatan birokrasi server.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet emerald">2</div>
            <div>
              <strong style="color: #ffffff;">Untuk Manajemen & Keuangan:</strong> Zero cost platform license dengan utilisasi server private Proxmox on-premise secara optimal.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet emerald">3</div>
            <div>
              <strong style="color: #ffffff;">Untuk Tim Infrastruktur:</strong> Operasional terpusat, kontrol resource jelas, bebas dari tiket konfigurasi Caddyfile/Nginx berulang.
            </div>
          </div>
        </div>
      </div>

      <div class="card highlight">
        <div class="card-title" style="color: #818cf8;">
          📍 Action Plan Selanjutnya (Tahap Adopsi)
        </div>
        <div class="list-stack">
          <div class="list-item">
            <div class="list-bullet">A</div>
            <div>
              <strong>Pilot Project & Uji Coba:</strong> Pelatihan perwakilan divisi non-tech & developer dengan Google Antigravity & Claude Code CLI.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet">B</div>
            <div>
              <strong>Automasi Maintenance:</strong> Penerapan cron job pembersih docker cache dan backup otomatis di server <code>192.168.10.21</code>.
            </div>
          </div>
          <div class="list-item">
            <div class="list-bullet">C</div>
            <div>
              <strong>Pusat Bantuan & Dukungan:</strong> Tim Infra membuka channel asistensi di Slack/Teams Proxsis untuk mendampingi deployment perdana.
            </div>
          </div>
        </div>
      </div>
    </div>

    <div style="text-align: center; margin-top: 10px; padding: 18px; background: rgba(30, 41, 59, 0.5); border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
      <div style="font-size: 20px; font-weight: 700; color: #ffffff;">
        Siap Mencoba? Akses <span style="color: #38bdf8;">https://connect.proxsis.com</span> & Mulai Deploy Proyek Anda Hari Ini! 🚀
      </div>
      <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">
        Dokumentasi & Konsultasi: Tim Cloud & AI Infra Proxsis (Mas Ulul & Rn)
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <div class="brand"><span>PROXSIS</span> INFRASTRUCTURE & AI ECOSYSTEM</div>
    <div>Selesai • Sesi Tanya Jawab (Q&A)</div>
    <div class="slide-number">13 / 13</div>
  </div>
</div>

</body>
</html>
"""

output_html = "/home/cleavers/Dokumen/coolify_new/SOSIALISASI_COOLIFY_SLIDES.html"
output_pdf = "/home/cleavers/Dokumen/coolify_new/SOSIALISASI_COOLIFY_SLIDES.pdf"

with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML slide successfully written to {output_html}")

# Generate PDF with Google Chrome Headless
chrome_cmd = [
    "google-chrome",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={output_pdf}",
    output_html
]

print("Compiling PDF with Google Chrome Headless...")
res = subprocess.run(chrome_cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"PDF successfully created: {output_pdf}")
else:
    print(f"Error creating PDF: {res.stderr}")
