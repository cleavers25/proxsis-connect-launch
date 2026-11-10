import os
import weasyprint

html_doc = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Blueprint Strategi & Sosialisasi Otomasi Deployment Coolify via AI Agent — Proxsis Group</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
    @top-right {
      content: "PROXSIS GROUP • CLOUD & AI INFRA";
      font-size: 7.5pt;
      font-weight: 700;
      color: #64748b;
      letter-spacing: 0.5px;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    @bottom-right {
      content: "Halaman " counter(page) " dari " counter(pages);
      font-size: 8pt;
      color: #64748b;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    @bottom-left {
      content: "Strategi & Sosialisasi Deployment Coolify • Dokumen Pengambilan Keputusan";
      font-size: 8pt;
      color: #64748b;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
  }

  * { box-sizing: border-box; }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.45;
    font-size: 8.5pt;
    margin: 0;
    padding: 0;
  }

  /* HEADER & HERO */
  .header-card {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    border-radius: 6px;
    padding: 14px 18px;
    margin-bottom: 12px;
    border-left: 5px solid #0284c7;
  }

  .badge-tag {
    display: inline-block;
    background: #0284c7;
    color: #ffffff;
    font-size: 7pt;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
  }

  .header-title {
    font-size: 14pt;
    font-weight: 800;
    margin: 0 0 4px 0;
    line-height: 1.25;
    color: #ffffff;
  }

  .header-subtitle {
    font-size: 8.5pt;
    color: #94a3b8;
    margin: 0 0 10px 0;
  }

  .meta-grid {
    display: table;
    width: 100%;
    border-top: 1px solid #334155;
    padding-top: 6px;
    font-size: 7.5pt;
    color: #cbd5e1;
  }

  .meta-col {
    display: table-cell;
    width: 33.33%;
  }

  .meta-col strong {
    color: #38bdf8;
  }

  /* TYPOGRAPHY & SECTIONS */
  h2 {
    font-size: 11pt;
    color: #0f172a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 3px;
    margin-top: 10px;
    margin-bottom: 8px;
    font-weight: 700;
  }

  p {
    margin: 0 0 6px 0;
  }

  /* CALLOUT BOXES */
  .callout-box {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #0284c7;
    border-radius: 5px;
    padding: 8px 12px;
    margin-bottom: 8px;
  }

  .callout-box.success {
    background-color: #f0fdf4;
    border-color: #bbf7d0;
    border-left-color: #10b981;
  }

  /* TABLES */
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0 10px 0;
    font-size: 7.5pt;
    page-break-inside: avoid;
  }

  table.data-table th {
    background-color: #0f172a;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #334155;
  }

  table.data-table td {
    padding: 5px 8px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
  }

  table.data-table tr:nth-child(even) td {
    background-color: #f8fafc;
  }

  /* BADGES */
  .status-pill {
    display: inline-block;
    padding: 2px 6px;
    border-radius: 10px;
    font-size: 6.5pt;
    font-weight: 700;
    text-transform: uppercase;
    white-space: nowrap;
  }

  .pill-green { background-color: #dcfce7; color: #166534; border: 1px solid #86efac; }
  .pill-yellow { background-color: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
  .pill-red { background-color: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }
  .pill-blue { background-color: #e0f2fe; color: #075985; border: 1px solid #7dd3fc; }

  /* CARDS GRID */
  .risk-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 8px 10px;
    margin-bottom: 7px;
    page-break-inside: avoid;
  }

  .risk-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3px;
  }

  .risk-title {
    font-weight: 700;
    color: #0f172a;
    font-size: 8pt;
  }

  .risk-desc {
    color: #475569;
    font-size: 7.5pt;
    margin-bottom: 4px;
    line-height: 1.35;
  }

  .risk-solution {
    background-color: #f0fdf4;
    border-left: 3px solid #10b981;
    padding: 4px 8px;
    font-size: 7.2pt;
    color: #14532d;
    line-height: 1.35;
  }

  /* ROADMAP STYLING */
  .phase-box {
    border: 1px solid #cbd5e1;
    background: #ffffff;
    border-radius: 5px;
    padding: 8px 10px;
    margin-bottom: 7px;
    page-break-inside: avoid;
  }

  .phase-header {
    font-weight: 700;
    font-size: 8pt;
    color: #0284c7;
    margin-bottom: 4px;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 2px;
  }

  ul.check-list {
    margin: 0;
    padding-left: 14px;
  }

  ul.check-list li {
    margin-bottom: 3px;
    font-size: 7.5pt;
    color: #334155;
    line-height: 1.35;
  }

  /* CODE BLOCK */
  pre.code-snippet {
    background-color: #0f172a;
    color: #e2e8f0;
    padding: 8px 10px;
    border-radius: 5px;
    font-size: 7pt;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    white-space: pre-wrap;
    word-break: break-all;
    line-height: 1.35;
    margin: 6px 0;
  }

  .page-break {
    page-break-after: always;
  }
</style>
</head>
<body>

  <!-- ================= PAGE 1 ================= -->
  <!-- HERO BANNER -->
  <div class="header-card">
    <div class="badge-tag">Blueprint Strategi Infra & AI 2026</div>
    <div class="header-title">Strategi & Sosialisasi Otomasi Deployment Coolify via AI Agent</div>
    <div class="header-subtitle">Analisis Akar Masalah, Standardisasi AI Agent, Manajemen Risiko Publik, dan Roadmap Implementasi</div>
    
    <div class="meta-grid">
      <div class="meta-col"><strong>Penulis:</strong> Rn (Cloud & AI Infra Team)</div>
      <div class="meta-col"><strong>Reviewer:</strong> Mas Ulul</div>
      <div class="meta-col"><strong>Target:</strong> Internal Proxsis & End-Users</div>
    </div>
  </div>

  <!-- SECTION 1 -->
  <h2>1. Latar Belakang & Analisis Akar Masalah (Root Cause: Kasus Mba Fahima)</h2>
  <div class="callout-box">
    <strong>Ringkasan Eksekutif:</strong> Tim Infra telah sukses membangun arsitektur deployment otomatis: Wildcard Cloudflare (*.connect.proxsis.com) &rarr; Reverse Proxy Caddy Host &rarr; VM Sitkrop Infra (Coolify / Traefik) tanpa perlu touch Caddyfile manual. Namun, friksi muncul saat user riil (seperti Mba Fahima) mencoba mengeksekusi otomatisasi melalui AI.
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 22%;">Platform AI</th>
        <th style="width: 26%;">Tipe Lingkungan</th>
        <th style="width: 22%;">Akses Eksekusi Shell</th>
        <th style="width: 30%;">Hasil Lapangan & Diagnosa</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Claude Desktop</strong></td>
        <td>GUI Desktop Terisolasi (Sandbox)</td>
        <td><span class="status-pill pill-red">Tidak Ada</span></td>
        <td><strong>Gagal Mandiri:</strong> AI hanya memberikan teks curl, user bingung mengeksekusi ke mana.</td>
      </tr>
      <tr>
        <td><strong>Google Antigravity</strong></td>
        <td>Agentic IDE / CLI Terintegrasi</td>
        <td><span class="status-pill pill-green">Native Shell Tool</span></td>
        <td><strong>Langsung Sukses ("Sung Bisa"):</strong> Agent mengeksekusi curl & API otomatis sampai live.</td>
      </tr>
      <tr>
        <td><strong>Kilo Code / Roo / Cline</strong></td>
        <td>VS Code Extension Agent</td>
        <td><span class="status-pill pill-green">Native Terminal Hook</span></td>
        <td><strong>Sukses:</strong> Berjalan lancar saat uji coba demo bersama Pak Ronny.</td>
      </tr>
      <tr>
        <td><strong>Claude Code (CLI)</strong></td>
        <td>Terminal CLI Resmi Anthropic</td>
        <td><span class="status-pill pill-green">Native Terminal</span></td>
        <td><strong>Solusi Pengguna Claude:</strong> Memakai akun Claude yang sama langsung di terminal CLI.</td>
      </tr>
    </tbody>
  </table>

  <!-- SECTION 2 -->
  <h2>2. Keputusan Standarisasi AI Agent (Tiering Support)</h2>
  <p>Untuk mencegah tim Infra kewalahan melayani troubleshooting puluhan varian tools AI, ditetapkan batasan resmi dukungan teknis:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 20%;">Tiering</th>
        <th style="width: 28%;">Platform / Agent</th>
        <th style="width: 24%;">Status Dukungan</th>
        <th style="width: 28%;">Rekomendasi Operasional</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tier 1 (Utama)</strong></td>
        <td><strong>Google Antigravity</strong></td>
        <td><span class="status-pill pill-green">Full Support (Default)</span></td>
        <td>Pilihan standar seluruh tim. Zero-config, eksekusi native, auto-recovery.</td>
      </tr>
      <tr>
        <td><strong>Tier 1 (Utama)</strong></td>
        <td><strong>Claude Code (CLI)</strong></td>
        <td><span class="status-pill pill-green">Full Support</span></td>
        <td>Wajib bagi pemilik akun Claude Pro/Team. Jalankan via <code>claude</code> di terminal.</td>
      </tr>
      <tr>
        <td><strong>Tier 1 (Dev)</strong></td>
        <td><strong>VS Code + Kilo Code / Cline</strong></td>
        <td><span class="status-pill pill-blue">Full Support (Devs)</span></td>
        <td>Khusus tim software engineer (sesuai demo Pak Ronny).</td>
      </tr>
      <tr>
        <td><strong>Tier 2 (Alternatif)</strong></td>
        <td><strong>Claude Desktop + Local MCP</strong></td>
        <td><span class="status-pill pill-yellow">Best-Effort</span></td>
        <td>Hanya jika user bersedia setup MCP Server terminal lokal (setup awal rumit).</td>
      </tr>
      <tr>
        <td><strong>Tier 3 (Ditolak)</strong></td>
        <td><strong>Claude Desktop Polosan / Web LLM</strong></td>
        <td><span class="status-pill pill-red">Unsupported</span></td>
        <td><strong>DILARANG untuk flow deploy otomatis</strong> karena tidak memiliki akses terminal.</td>
      </tr>
    </tbody>
  </table>

  <div class="callout-box success">
    <strong>💡 Kebijakan Operasional Pengguna Claude:</strong> Jangan biarkan user memakai Claude Desktop polosan! Cukup arahkan user menginstal <strong>Claude Code CLI</strong>: <code>npm install -g @anthropic-ai/claude-code</code> &rarr; jalankan <code>claude</code> &rarr; login dengan akun Claude yang sama.
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 2 ================= -->
  <!-- SECTION 3 -->
  <h2>3. Identifikasi Concern & Mitigasi Risiko (Jika Digunakan Publik / Lintas Divisi)</h2>
  <p>Jika pipeline Coolify ini dibuka ke publik atau lintas unit bisnis Proxsis, terdapat 5 risiko krusial yang wajib dikontrol:</p>

  <div class="risk-card">
    <div class="risk-header">
      <span class="risk-title">1. Keamanan Kredensial & Kebocoran Token (CRITICAL 🔴)</span>
      <span class="status-pill pill-red">Risiko Tinggi</span>
    </div>
    <div class="risk-desc">Token Coolify (<code>COOLIFY_TOKEN</code>) saat ini bersifat master/admin. Jika dibagikan mentah, user bisa sengaja atau tidak sengaja melihat, menghentikan, atau menghapus container milik project/divisi lain.</div>
    <div class="risk-solution"><strong>Mitigasi:</strong> Terapkan pembagian Team/Project RBAC di Coolify. Untuk skala publik, sediakan Deploy-Gateway (API jembatan) agar token master tidak pernah dibagikan ke client.</div>
  </div>

  <div class="risk-card">
    <div class="risk-header">
      <span class="risk-title">2. Tabrakan Nama Subdomain (Domain Collision) (HIGH 🟠)</span>
      <span class="status-pill pill-yellow">Risiko Sedang-Tinggi</span>
    </div>
    <div class="risk-desc">Jika dua pengguna mendaftarkan nama yang sama (misal <code>landing.connect.proxsis.com</code>), Traefik akan mengalami konflik routing dan salah satu aplikasi tidak dapat diakses.</div>
    <div class="risk-solution"><strong>Mitigasi:</strong> Wajibkan standar penamaan otomatis oleh AI Agent: <code>https://[divisi]-[nama_user]-[namaproject].connect.proxsis.com</code>.</div>
  </div>

  <div class="risk-card">
    <div class="risk-header">
      <span class="risk-title">3. Penumpukan Container Zombie & Storage Penuh (HIGH 🟠)</span>
      <span class="status-pill pill-yellow">Risiko Resource</span>
    </div>
    <div class="risk-desc">User melakukan puluhan kali eksperimen deployment lalu ditinggalkan begitu saja. RAM VM Proxmox (Sitkrop Infra) dan disk space Docker image akan cepat terkuras habis.</div>
    <div class="risk-solution"><strong>Mitigasi:</strong> Pasang default resource limit (Max 512MB RAM & 0.5 CPU) serta aktifkan cron job pembersih otomatis: <code>docker image prune -af --filter "until=72h"</code>.</div>
  </div>

  <div class="risk-card">
    <div class="risk-header">
      <span class="risk-title">4. Cloudflare WAF Block (HTTP 403) (MEDIUM 🟡)</span>
      <span class="status-pill pill-blue">Risiko Konektivitas</span>
    </div>
    <div class="risk-desc">Cloudflare WAF di domain <code>connect.proxsis.com</code> memblokir request API otomatis jika tidak memiliki User-Agent browser/curl yang valid.</div>
    <div class="risk-solution"><strong>Mitigasi:</strong> Wajibkan flag <code>-H "User-Agent: curl/8.5.0"</code> di seluruh prompt dan script automasi AI Agent.</div>
  </div>

  <div class="risk-card">
    <div class="risk-header">
      <span class="risk-title">5. Multi-tenancy & Isolasi Lingkungan (MEDIUM 🟡)</span>
      <span class="status-pill pill-blue">Risiko Tata Kelola</span>
    </div>
    <div class="risk-desc">Aplikasi produksi internal bercampur dengan aplikasi latihan/coba-coba dalam satu dashboard project.</div>
    <div class="risk-solution"><strong>Mitigasi:</strong> Pisahkan minimal 2 lingkungan di Coolify: <code>Sandbox & R&D</code> (auto-cleanup aktif) dan <code>Internal Production</code> (akses terbatas).</div>
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 3 ================= -->
  <!-- SECTION 4 -->
  <h2>4. Action Plan & Roadmap Implementasi</h2>

  <div class="phase-box">
    <div class="phase-header">Fase 1: Standarisasi Tooling & Onboarding (Minggu 1)</div>
    <ul class="check-list">
      <li>Resmikan SOP pemilihan AI Agent (Antigravity & Claude Code CLI sebagai standar utama).</li>
      <li>Perbarui panduan <code>AI_DEPLOYMENT_CONFIG.md</code> dengan format subdomain anti-tabrakan.</li>
      <li>Sediakan script onboarding 1 baris untuk laptop tim internal: <code>curl -fsSL https://connect.proxsis.com/setup-agent.sh | bash</code></li>
    </ul>
  </div>

  <div class="phase-box">
    <div class="phase-header">Fase 2: Infra Guardrails & Limitasi Resource (Minggu 2)</div>
    <ul class="check-list">
      <li>Setup Project Hierarchy di Coolify: Pisahkan Environment Sandbox vs Production.</li>
      <li>Terapkan Resource Limiter: Batasi default container ke 512MB RAM dan 0.5 CPU Core.</li>
      <li>Pasang Cron Job Docker Garbage Collection di server Proxmox <code>192.168.10.21</code>.</li>
    </ul>
  </div>

  <div class="phase-box">
    <div class="phase-header">Fase 3: Sosialisasi Pilot & Uji Coba Terarah (Minggu 3)</div>
    <ul class="check-list">
      <li>Uji coba pilot run dengan Mba Fahima (persona non-tech) dan Pak Ronny (persona developer / Kilo Code).</li>
      <li>Evaluasi friction points dan rilis cheat-sheet 3 langkah: <em>"Buka folder &rarr; Ketik 'Deploy ke Coolify' &rarr; Dapatkan link *.connect.proxsis.com"</em>.</li>
    </ul>
  </div>

  <div class="phase-box">
    <div class="phase-header">Fase 4: Skalabilitas Publik & Audit Governance (Minggu 4+)</div>
    <ul class="check-list">
      <li>Rancang arsitektur <em>Deploy-Gateway API</em> jika infrastruktur dibuka untuk publik eksternal (mencegah eksposur token Coolify).</li>
      <li>Setup monitoring kapasitas VM Sitkrop Infra via dashboard Coolify & alert Telegram/Discord.</li>
    </ul>
  </div>

  <!-- SECTION 5 -->
  <h2>5. Lampiran: Draft Keputusan Eksekutif untuk Mas Ulul</h2>
  <pre class="code-snippet">
Siap Mas Ulul, ini hasil analisa dan keputusan solusinya:

1. KEPUTUSAN SUPPORT AGENT:
Kita fix tetapkan standard resmi:
- Tier 1 (Utama): Google Antigravity & Claude Code (CLI).
- Tier Developer: VS Code + Kilo Code (seperti demo Pak Ronny).
- Claude Desktop polosan resmi dicoret untuk flow deploy karena murni GUI sandbox tanpa terminal. 
  User Claude dialihkan pakai 'Claude Code CLI' (pakai akun Claude yg sama).

2. CONCERN UTAMA JIKA DIGUNAKAN PUBLIK / LINTAS TIM:
- Token Security: Token Coolify jangan dibagi mentah jika mau dipakai publik luas (rawan hapus project).
- Subdomain Collision: Wajib format [user]-[project].connect.proxsis.com agar routing proxy tidak bentrok.
- Server Resource (Sitkrop Infra): Wajib auto-cleanup image dan limit RAM 512MB per app agar VM tidak overload.
- Cloudflare WAF: Header curl harus konsisten agar tidak terkena blokir HTTP 403.

3. ACTION PLAN:
- Minggu 1: Kunci template instruksi AI, sediakan 1-line script onboarding agent.
- Minggu 2: Setting resource limit & auto-prune di Coolify server.
- Minggu 3: Sosialisasi pilot run ke Mba Fahima & tim Pak Ronny.
  </pre>

  <div style="text-align: center; color: #94a3b8; font-size: 7.5pt; margin-top: 10px;">
    Dokumen Cetak Resmi &bull; Proxsis Group Managed IT Infrastructure &bull; 2026
  </div>

</body>
</html>
"""

html_path = "/home/cleavers/Dokumen/coolify_new/STRATEGI_SOSIALISASI_COOLIFY_AI.html"
pdf_path = "/home/cleavers/Dokumen/coolify_new/STRATEGI_SOSIALISASI_COOLIFY_AI.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_doc)

print(f"HTML generated at {html_path}")
print("Rendering PDF with WeasyPrint...")
doc = weasyprint.HTML(filename=html_path)
doc.write_pdf(pdf_path)
print(f"PDF generated successfully at {pdf_path}")
print(f"PDF size: {os.path.getsize(pdf_path)} bytes")
