import os
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1280
HEIGHT = 720
FPS = 30
TOTAL_DURATION = 92 # seconds
TOTAL_FRAMES = TOTAL_DURATION * FPS

# Load fonts
FONT_REGULAR = "/usr/share/fonts/google-noto/NotoSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/google-noto/NotoSans-Bold.ttf"

font_title_lg = ImageFont.truetype(FONT_BOLD, 36)
font_title_md = ImageFont.truetype(FONT_BOLD, 26)
font_subtitle = ImageFont.truetype(FONT_REGULAR, 19)
font_body_bold = ImageFont.truetype(FONT_BOLD, 17)
font_body = ImageFont.truetype(FONT_REGULAR, 15)
font_badge = ImageFont.truetype(FONT_BOLD, 14)
font_small = ImageFont.truetype(FONT_REGULAR, 13)
font_mono = ImageFont.truetype(FONT_BOLD, 15)

# Screenshot pre-loading & pre-caching
screenshot_paths = {
    "projects": "/home/cleavers/Deploy Coolify/Screenshot_20261017_142956.png",
    "env_add": "/home/cleavers/Deploy Coolify/Screenshot_20261017_143154.png",
    "github_connected": "/home/cleavers/Deploy Coolify/Screenshot_20261017_143732.png",
    "select_repo": "/home/cleavers/Deploy Coolify/Screenshot_20261017_144009.png",
    "deploy_logs": "/home/cleavers/Deploy Coolify/Screenshot_20261017_144213.png",
    "running_green": "/home/cleavers/Deploy Coolify/Screenshot_20261017_145454.png",
    "domain_input": "/home/cleavers/Deploy Coolify/Screenshot_20261017_145642.png",
    "redeploy_ready": "/home/cleavers/Deploy Coolify/Screenshot_20261017_145806.png",
}

cached_images = {}
for key, p in screenshot_paths.items():
    if os.path.exists(p):
        img = Image.open(p).convert("RGB")
        # Resize to fit main view area (max width 980, max height 490)
        img.thumbnail((980, 480), Image.Resampling.LANCZOS)
        cached_images[key] = img

print(f"Loaded {len(cached_images)} cached screenshots.")

def draw_header(draw, title_text, chapter_badge, frame_idx):
    # Top banner background
    draw.rectangle([0, 0, WIDTH, 54], fill="#090d16")
    draw.line([0, 54, WIDTH, 54], fill="#1e293b", width=1)
    
    # Logo / Org badge
    draw.rounded_rectangle([20, 11, 145, 42], radius=4, fill="#0284c7")
    draw.text((32, 18), "PROXSIS PaaS", fill="#ffffff", font=font_badge)
    
    # Chapter badge
    draw.rounded_rectangle([155, 11, 265, 42], radius=4, fill="#1e293b", outline="#334155")
    draw.text((165, 18), chapter_badge, fill="#38bdf8", font=font_badge)
    
    # Title text
    draw.text((280, 16), title_text, fill="#f8fafc", font=font_body_bold)
    
    # Animated progress bar at bottom of header
    progress = frame_idx / TOTAL_FRAMES
    bar_w = int(WIDTH * progress)
    draw.line([0, 54, bar_w, 54], fill="#38bdf8", width=3)

def draw_subtitle_card(draw, badge_text, main_text, sub_text, badge_color="#0284c7"):
    card_y1 = 605
    card_y2 = 705
    # Translucent styled card
    draw.rounded_rectangle([20, card_y1, WIDTH - 20, card_y2], radius=8, fill="#0f172a", outline="#334155", width=1)
    
    # Badge
    draw.rounded_rectangle([35, card_y1 + 12, 160, card_y1 + 38], radius=4, fill=badge_color)
    draw.text((45, card_y1 + 16), badge_text, fill="#ffffff", font=font_badge)
    
    # Texts
    draw.text((175, card_y1 + 14), main_text, fill="#f8fafc", font=font_body_bold)
    draw.text((35, card_y1 + 46), sub_text, fill="#94a3b8", font=font_body)

# FFmpeg command
mp4_out = "/home/cleavers/Dokumen/coolify_new/Panduan_Deployment_Coolify_Animasi.mp4"
wav_in = "/home/cleavers/Dokumen/coolify_new/soundtrack.wav"

ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-f", "rawvideo",
    "-vcodec", "rawvideo",
    "-s", f"{WIDTH}x{HEIGHT}",
    "-pix_fmt", "bgr24",
    "-r", str(FPS),
    "-i", "-", # stdin
    "-i", wav_in,
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-pix_fmt", "yuv420p",
    "-crf", "22",
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    mp4_out
]

proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

print("Starting video frame rendering...")

for f in range(TOTAL_FRAMES):
    sec = f / FPS
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0b0f19")
    draw = ImageDraw.Draw(img)
    
    # -------------------------------------------------------------------------
    # SCENE 1: INTRO (0 to 6s)
    # -------------------------------------------------------------------------
    if sec < 6.0:
        # Subtle moving grid lines
        t_offset = int((f * 2) % 40)
        for gy in range(0, HEIGHT, 40):
            draw.line([0, gy + t_offset, WIDTH, gy + t_offset], fill="#111827", width=1)
            
        # Glowing center card
        cx, cy = WIDTH // 2, HEIGHT // 2 - 20
        draw.rounded_rectangle([cx - 420, cy - 160, cx + 420, cy + 180], radius=16, fill="#0f172a", outline="#0284c7", width=2)
        
        # Pill
        draw.rounded_rectangle([cx - 130, cy - 135, cx + 130, cy - 100], radius=18, fill="#0284c7")
        draw.text((cx - 105, cy - 128), "PROXSIS MANAGED INFRA", fill="#ffffff", font=font_badge)
        
        # Title
        draw.text((cx - 360, cy - 75), "PANDUAN DEPLOYMENT COOLIFY", fill="#38bdf8", font=font_title_lg)
        draw.text((cx - 330, cy - 25), "Edisi Animasi & Panduan Interaktif Lengkap", fill="#f8fafc", font=font_title_md)
        
        # Subtitle
        draw.text((cx - 380, cy + 30), "Deploy Aplikasi Web & API Instan • Otomatis Wildcard Proxy • Bebas Edit Caddyfile", fill="#94a3b8", font=font_subtitle)
        
        # 3 Badges appearing sequentially
        if sec > 1.5:
            draw.rounded_rectangle([cx - 340, cy + 85, cx - 130, cy + 125], radius=6, fill="#1e293b", outline="#38bdf8")
            draw.text((cx - 320, cy + 96), "⚡ AI Agent Auto-Deploy", fill="#38bdf8", font=font_badge)
        if sec > 2.5:
            draw.rounded_rectangle([cx - 105, cy + 85, cx + 105, cy + 125], radius=6, fill="#1e293b", outline="#10b981")
            draw.text((cx - 90, cy + 96), "🌐 *.connect.proxsis.com", fill="#34d399", font=font_badge)
        if sec > 3.5:
            draw.rounded_rectangle([cx + 130, cy + 85, cx + 340, cy + 125], radius=6, fill="#1e293b", outline="#f59e0b")
            draw.text((cx + 150, cy + 96), "🖥️ Dashboard UI Mandiri", fill="#fbbf24", font=font_badge)
            
        draw_subtitle_card(draw, "MEMULAI", "Selamat Datang di Panduan Deployment Coolify Proxsis Group", "Video ini menyajikan alur lengkap otomatisasi AI Agent & 27 langkah UI Dashboard.")

    # -------------------------------------------------------------------------
    # SCENE 2: ARSITEKTUR JARINGAN & WILDCARD (6 to 22s)
    # -------------------------------------------------------------------------
    elif sec < 22.0:
        draw_header(draw, "Bagian 1: Arsitektur Jaringan Wildcard Reverse Proxy", "ARSITEKTUR", f)
        
        # Draw 5 Pipeline Nodes
        nodes = [
            ("Pengunjung", "Browser Pengguna\nHTTPS Request", "#38bdf8", 70),
            ("Cloudflare", "*.connect.proxsis.com\nDNS Wildcard + SSL", "#f59e0b", 310),
            ("VPS Caddy Host", "143.20.49.131\nReverse Proxy Host", "#818cf8", 550),
            ("Sitkrop Infra", "192.168.10.21\nCoolify Traefik Hub", "#10b981", 790),
            ("Aplikasi Web", "Container Docker\nBerjalan Otomatis", "#22c55e", 1030),
        ]
        
        box_y = 130
        box_w = 175
        box_h = 100
        
        # Connectors
        for i in range(len(nodes) - 1):
            x1 = nodes[i][3] + box_w
            x2 = nodes[i+1][3]
            draw.line([x1, box_y + box_h // 2, x2, box_y + box_h // 2], fill="#334155", width=3)
            
        # Animated traveling data packet
        packet_anim = ((sec - 6.0) * 120) % (nodes[-1][3] - nodes[0][3])
        px = int(nodes[0][3] + box_w // 2 + packet_anim)
        draw.ellipse([px - 8, box_y + box_h // 2 - 8, px + 8, box_y + box_h // 2 + 8], fill="#38bdf8", outline="#ffffff", width=2)
        
        # Draw Nodes
        for title, desc, color, nx in nodes:
            # Highlight node 4 (Sitkrop Infra) with glow border
            is_sitkrop = (title == "Sitkrop Infra")
            border_w = 3 if is_sitkrop else 1
            border_c = "#34d399" if is_sitkrop else "#334155"
            bg_c = "#064e3b" if is_sitkrop else "#0f172a"
            
            draw.rounded_rectangle([nx, box_y, nx + box_w, box_y + box_h], radius=8, fill=bg_c, outline=border_c, width=border_w)
            draw.text((nx + 12, box_y + 12), title, fill=color, font=font_body_bold)
            
            lines = desc.split("\n")
            draw.text((nx + 12, box_y + 40), lines[0], fill="#f8fafc", font=font_small)
            draw.text((nx + 12, box_y + 60), lines[1], fill="#94a3b8", font=font_small)

        # Highlight Explanation Card below
        draw.rounded_rectangle([70, 270, WIDTH - 70, 570], radius=10, fill="#0f172a", outline="#1e293b")
        
        draw.rounded_rectangle([95, 290, 420, 325], radius=6, fill="#0284c7")
        draw.text((105, 298), "KENAPA TIDAK PERLU EDIT CADDYFILE MANUAL?", fill="#ffffff", font=font_badge)
        
        points = [
            "1. Caddy di VPS Utama (143.20.49.131) sudah dipasangi rule permanen wildcard:",
            "   *.connect.proxsis.com -> reverse_proxy 192.168.10.21:80",
            "2. Coolify Traefik di server Sitkrop Infra (192.168.10.21) membaca label domain container secara otomatis.",
            "3. Traefik otomatis membuatkan sertifikat SSL dan routing ke port container yang Anda buka.",
            "4. DILARANG atau TIDAK PERLU lagi mengubah file /etc/caddy/Caddyfile selamanya!"
        ]
        
        py = 345
        for p in points:
            color = "#f59e0b" if "DILARANG" in p else ("#38bdf8" if "192.168.10.21" in p else "#f8fafc")
            font_to_use = font_mono if p.startswith("   ") else font_body
            draw.text((100, py), p, fill=color, font=font_to_use)
            py += 36
            
        draw_subtitle_card(draw, "ATURAN EMAS", "Wajib Deploy ke Sitkrop Infra (192.168.10.21) & Domain *.connect.proxsis.com", "Rantai otomatisasi ini bekerja 100% tanpa campur tangan teknis manual di sisi server.", "#059669")

    # -------------------------------------------------------------------------
    # SCENE 3: METODE 1 - AI AGENT AUTO-DEPLOY (22 to 42s)
    # -------------------------------------------------------------------------
    elif sec < 42.0:
        draw_header(draw, "Bagian 2: Otomatisasi Deployment Instan via AI Agent", "AI AGENT", f)
        
        # Left box: AI_DEPLOYMENT_CONFIG.md file mockup
        draw.rounded_rectangle([60, 80, 520, 570], radius=8, fill="#0f172a", outline="#334155")
        draw.rounded_rectangle([60, 80, 520, 120], radius=8, fill="#1e293b")
        draw.text((80, 92), "📄 AI_DEPLOYMENT_CONFIG.md", fill="#38bdf8", font=font_body_bold)
        
        code_lines = [
            "# Cukup isi 2 token ini (1x Konfigurasi):",
            "",
            "GITHUB_TOKEN=\"ghp_v47x991...\"",
            "COOLIFY_TOKEN=\"9|bQbRxbXqCN...\"",
            "",
            "# URL Repo GitHub (Boleh Dikosongkan):",
            "GIT_REPOSITORY=\"\"",
            "",
            "# File ini aman karena sudah ada di .gitignore",
            "# Token tidak akan pernah bocor ke publik!"
        ]
        
        cy = 140
        for cl in code_lines:
            col = "#34d399" if "TOKEN=" in cl else ("#64748b" if cl.startswith("#") else "#f8fafc")
            draw.text((80, cy), cl, fill=col, font=font_mono)
            cy += 28

        # Right box: Chat prompt & automated execution
        draw.rounded_rectangle([550, 80, WIDTH - 60, 570], radius=8, fill="#0f172a", outline="#0284c7")
        draw.rounded_rectangle([550, 80, WIDTH - 60, 120], radius=8, fill="#0284c7")
        draw.text((570, 92), "💬 CHAT PROMPT KE AI AGENT", fill="#ffffff", font=font_body_bold)
        
        # Chat bubble user
        draw.rounded_rectangle([570, 140, WIDTH - 80, 210], radius=8, fill="#1e293b", outline="#38bdf8")
        draw.text((585, 150), "User:", fill="#38bdf8", font=font_badge)
        
        # Animated typing prompt
        full_prompt = "“Tolong deploy website di folder ini ke Coolify dengan domain https://synergi.connect.proxsis.com”"
        chars_to_show = min(len(full_prompt), int((sec - 23.0) * 45)) if sec > 23.0 else 0
        draw.text((585, 175), full_prompt[:chars_to_show], fill="#ffffff", font=font_body)
        
        # AI Response Card
        if sec > 27.0:
            draw.rounded_rectangle([570, 230, WIDTH - 80, 540], radius=8, fill="#090d16", outline="#10b981")
            draw.text((585, 245), "🤖 AI Agent Eksekusi:", fill="#34d399", font=font_badge)
            
            steps_ai = [
                ("[✔] 1. Mendeteksi project & push ke GitHub repositori...", "#94a3b8", 280),
                ("[✔] 2. Menghubungi API Coolify connect.proxsis.com...", "#94a3b8", 320),
                ("[✔] 3. Mendaftarkan aplikasi ke server Sitkrop Infra...", "#94a3b8", 360),
                ("[✔] 4. Memasang SSL & domain synergi.connect.proxsis.com...", "#94a3b8", 400),
            ]
            for txt, c, sy in steps_ai:
                draw.text((585, sy), txt, fill=c, font=font_body)
                
            # Result Banner
            if sec > 32.0:
                draw.rounded_rectangle([585, 450, WIDTH - 95, 520], radius=6, fill="#065f46", outline="#34d399", width=2)
                draw.text((605, 462), "🚀 DEPLOYMENT BERHASIL! STATUS: RUNNING (HIJAU)", fill="#34d399", font=font_body_bold)
                draw.text((605, 490), "🔗 https://synergi.connect.proxsis.com", fill="#ffffff", font=font_body_bold)
                
        draw_subtitle_card(draw, "1-KLIK DEPLOY", "AI Agent Menangani Git Push, API Coolify, Traefik & Domain Otomatis", "Cukup berikan 1 kalimat instruksi di chat, sistem langsung online dalam hitungan detik.")

    # -------------------------------------------------------------------------
    # SCENE 4: METODE 2 - MANUAL DASHBOARD WALKTHROUGH (42 to 74s)
    # -------------------------------------------------------------------------
    elif sec < 74.0:
        # We split into 5 sub-stages:
        # 4A (42-48): Projects & Add (+ Add button)
        # 4B (48-55): Add Resource GitHub App
        # 4C (55-61): Select Repo & Branch
        # 4D (61-68): Deploy & Running Status
        # 4E (68-74): Subdomain Setting & Redeploy
        
        pulse = int(np.sin((sec * 10)) * 3)
        
        if sec < 48.0:
            draw_header(draw, "Bagian 3: Panduan UI — Langkah 01-03: Menambahkan Project & Environment", "UI DASHBOARD", f)
            shot = cached_images.get("projects")
            if shot:
                sx, sy = (WIDTH - shot.width) // 2, 80
                img.paste(shot, (sx, sy))
                draw.rectangle([sx - 2, sy - 2, sx + shot.width + 1, sy + shot.height + 1], outline="#38bdf8", width=1)
                
                # Highlight "+ Add" button (around top right of screenshot)
                btn_x1 = sx + int(shot.width * 0.88)
                btn_y1 = sy + int(shot.height * 0.08)
                btn_x2 = sx + int(shot.width * 0.96)
                btn_y2 = sy + int(shot.height * 0.16)
                draw.rectangle([btn_x1 - pulse, btn_y1 - pulse, btn_x2 + pulse, btn_y2 + pulse], outline="#ef4444", width=3)
                
            draw_subtitle_card(draw, "LANGKAH 01-03", "Masuk ke Menu Projects & Klik Tombol '+ Add' di Kanan Atas", "Beri nama project (misal: PT Synergi atau PT Proxsis), lalu buka kartu environment 'production'.")

        elif sec < 55.0:
            draw_header(draw, "Bagian 3: Panduan UI — Langkah 04-12: Integrasi Sumber Kode GitHub App", "UI DASHBOARD", f)
            shot = cached_images.get("env_add")
            if shot:
                sx, sy = (WIDTH - shot.width) // 2, 80
                img.paste(shot, (sx, sy))
                draw.rectangle([sx - 2, sy - 2, sx + shot.width + 1, sy + shot.height + 1], outline="#38bdf8", width=1)
                
                # Highlight "Private Repository" card
                btn_x1 = sx + int(shot.width * 0.05)
                btn_y1 = sy + int(shot.height * 0.35)
                btn_x2 = sx + int(shot.width * 0.45)
                btn_y2 = sy + int(shot.height * 0.58)
                draw.rectangle([btn_x1 - pulse, btn_y1 - pulse, btn_x2 + pulse, btn_y2 + pulse], outline="#ef4444", width=3)
                
            draw_subtitle_card(draw, "LANGKAH 04-12", "Pilih 'Private Repository' & Hubungkan GitHub App (Cukup 1x Setup)", "Otorisasi akun GitHub Anda ke Coolify. Status akan berubah menjadi hijau ('Connected').")

        elif sec < 61.0:
            draw_header(draw, "Bagian 3: Panduan UI — Langkah 13-18: Memilih Repositori & Branch Utama", "UI DASHBOARD", f)
            shot = cached_images.get("select_repo")
            if shot:
                sx, sy = (WIDTH - shot.width) // 2, 80
                img.paste(shot, (sx, sy))
                draw.rectangle([sx - 2, sy - 2, sx + shot.width + 1, sy + shot.height + 1], outline="#38bdf8", width=1)
                
                # Highlight repo selector
                btn_x1 = sx + int(shot.width * 0.28)
                btn_y1 = sy + int(shot.height * 0.32)
                btn_x2 = sx + int(shot.width * 0.72)
                btn_y2 = sy + int(shot.height * 0.52)
                draw.rectangle([btn_x1 - pulse, btn_y1 - pulse, btn_x2 + pulse, btn_y2 + pulse], outline="#38bdf8", width=3)
                
            draw_subtitle_card(draw, "LANGKAH 13-18", "Pilih Nama Repositori & Branch Utama ('main' atau 'master')", "Coolify otomatis mendeteksi stack (Nixpacks/Railpack/Dockerfile) tanpa perlu file config tambahan.")

        elif sec < 68.0:
            draw_header(draw, "Bagian 3: Panduan UI — Langkah 21-23: Jalankan Deploy & Verifikasi Running", "UI DASHBOARD", f)
            shot = cached_images.get("running_green")
            if shot:
                sx, sy = (WIDTH - shot.width) // 2, 80
                img.paste(shot, (sx, sy))
                draw.rectangle([sx - 2, sy - 2, sx + shot.width + 1, sy + shot.height + 1], outline="#10b981", width=1)
                
                # Highlight "Running" badge at top right
                btn_x1 = sx + int(shot.width * 0.82)
                btn_y1 = sy + int(shot.height * 0.05)
                btn_x2 = sx + int(shot.width * 0.98)
                btn_y2 = sy + int(shot.height * 0.15)
                draw.rectangle([btn_x1 - pulse, btn_y1 - pulse, btn_x2 + pulse, btn_y2 + pulse], outline="#22c55e", width=3)
                
            draw_subtitle_card(draw, "LANGKAH 21-23", "Klik Tombol 'Deploy' & Pastikan Status Berubah Menjadi 'Running' (Hijau)", "Layar log akan menampilkan proses clone & build. Saat status hijau, aplikasi sudah aktif sempurna!")

        else:
            draw_header(draw, "Bagian 3: Panduan UI — Langkah 24-27: Pasang Subdomain Resmi & Redeploy", "UI DASHBOARD", f)
            shot = cached_images.get("domain_input")
            if shot:
                sx, sy = (WIDTH - shot.width) // 2, 80
                img.paste(shot, (sx, sy))
                draw.rectangle([sx - 2, sy - 2, sx + shot.width + 1, sy + shot.height + 1], outline="#0284c7", width=1)
                
                # Highlight domain input field
                btn_x1 = sx + int(shot.width * 0.28)
                btn_y1 = sy + int(shot.height * 0.45)
                btn_x2 = sx + int(shot.width * 0.82)
                btn_y2 = sy + int(shot.height * 0.65)
                draw.rectangle([btn_x1 - pulse, btn_y1 - pulse, btn_x2 + pulse, btn_y2 + pulse], outline="#0284c7", width=3)
                
            draw_subtitle_card(draw, "LANGKAH 24-27", "Isi Domain: https://<nama-aplikasi>.connect.proxsis.com -> Klik Redeploy!", "Status 'Changes pending' bukan error. Cukup klik Redeploy untuk menerapkan domain ke Traefik.")

    # -------------------------------------------------------------------------
    # SCENE 5: STRATEGI MULTI-PT & SHARING SERVER (74 to 84s)
    # -------------------------------------------------------------------------
    elif sec < 84.0:
        draw_header(draw, "Bagian 4: Strategi Manajemen Multi-PT & Sharing Server", "MULTI-PT", f)
        
        # Root Team Box
        draw.rounded_rectangle([420, 80, 860, 160], radius=8, fill="#0f172a", outline="#0284c7", width=2)
        draw.text((440, 95), "TEAM: PROXSIS GROUP", fill="#38bdf8", font=font_body_bold)
        draw.text((440, 125), "Server Bersama: Sitkrop Infra (192.168.10.21)", fill="#f8fafc", font=font_body)
        
        # Branch lines
        draw.line([540, 160, 300, 240], fill="#38bdf8", width=3)
        draw.line([740, 160, 980, 240], fill="#38bdf8", width=3)
        
        # Branch Left: PT Proxsis & Co
        draw.rounded_rectangle([120, 240, 480, 450], radius=8, fill="#0f172a", outline="#818cf8", width=2)
        draw.text((140, 255), "PROJECT: PT PROXSIS & CO", fill="#818cf8", font=font_body_bold)
        draw.text((140, 290), "• Web Portal (Next.js)", fill="#f8fafc", font=font_body)
        draw.text((140, 325), "• ERP Service (Laravel)", fill="#f8fafc", font=font_body)
        draw.text((140, 360), "• PostgreSQL Database", fill="#f8fafc", font=font_body)
        draw.text((140, 395), "Domain: https://proxsis.connect.proxsis.com", fill="#38bdf8", font=font_small)
        
        # Branch Right: PT Synergi
        draw.rounded_rectangle([800, 240, 1160, 450], radius=8, fill="#0f172a", outline="#34d399", width=2)
        draw.text((820, 255), "PROJECT: PT SYNERGI", fill="#34d399", font=font_body_bold)
        draw.text((820, 290), "• Landing Page PT Synergi", fill="#f8fafc", font=font_body)
        draw.text((820, 325), "• Core API Backend", fill="#f8fafc", font=font_body)
        draw.text((820, 360), "• Redis Cache Storage", fill="#f8fafc", font=font_body)
        draw.text((820, 395), "Domain: https://synergi.connect.proxsis.com", fill="#34d399", font=font_small)
        
        # Bottom Tip Box
        draw.rounded_rectangle([120, 480, 1160, 560], radius=8, fill="#1e293b", outline="#334155")
        draw.text((140, 495), "💡 Tips Arsitektur Multi-PT:", fill="#fbbf24", font=font_badge)
        draw.text((140, 525), "1 Server fisik bisa memuat banyak Project PT! Jika butuh isolasi hak akses total antar developer, buat VM baru di Proxmox.", fill="#e2e8f0", font=font_small)
        
        draw_subtitle_card(draw, "ARSITEKTUR PT", "Gunakan 1 Project Khusus untuk Setiap PT Agar Berbagi Server dengan Rapi", "Aplikasi dan database antar PT tetap terisolasi dalam namespace project masing-masing.", "#7c3aed")

    # -------------------------------------------------------------------------
    # SCENE 6: 2 ATURAN EMAS & OUTRO (84 to 92s)
    # -------------------------------------------------------------------------
    else:
        draw_header(draw, "Ringkasan: 2 Aturan Emas Deployment Proxsis", "KESIMPULAN", f)
        
        # Golden Card 1
        draw.rounded_rectangle([100, 100, 600, 380], radius=10, fill="#0f172a", outline="#10b981", width=2)
        draw.rounded_rectangle([100, 100, 600, 150], radius=10, fill="#065f46")
        draw.text((120, 115), "ATURAN EMAS 1: TARGET SERVER", fill="#ffffff", font=font_body_bold)
        draw.text((120, 180), "Selalu Pilih Server:", fill="#94a3b8", font=font_body)
        draw.text((120, 215), "Sitkrop Infra / Proxsis-Coolify", fill="#34d399", font=font_title_md)
        draw.text((120, 260), "IP: 192.168.10.21 (Port: 22)", fill="#f8fafc", font=font_body)
        draw.text((120, 300), "Traefik di server ini yang otomatis memproses", fill="#cbd5e1", font=font_small)
        draw.text((120, 325), "seluruh rute & SSL tanpa konfigurasi manual.", fill="#cbd5e1", font=font_small)
        
        # Golden Card 2
        draw.rounded_rectangle([680, 100, 1180, 380], radius=10, fill="#0f172a", outline="#0284c7", width=2)
        draw.rounded_rectangle([680, 100, 1180, 150], radius=10, fill="#0284c7")
        draw.text((700, 115), "ATURAN EMAS 2: FORMAT DOMAIN", fill="#ffffff", font=font_body_bold)
        draw.text((700, 180), "Selalu Gunakan Akhiran:", fill="#94a3b8", font=font_body)
        draw.text((700, 215), "*.connect.proxsis.com", fill="#38bdf8", font=font_title_md)
        draw.text((700, 260), "Contoh: https://app.connect.proxsis.com", fill="#f8fafc", font=font_body)
        draw.text((700, 300), "Otomatis di-routing oleh Cloudflare & Caddy", fill="#cbd5e1", font=font_small)
        draw.text((700, 325), "sehingga domain langsung aktif seketika.", fill="#cbd5e1", font=font_small)
        
        # Outro banner
        draw.rounded_rectangle([100, 420, 1180, 560], radius=10, fill="#1e293b", outline="#334155")
        draw.text((450, 445), "Selamat Mencoba Deployment di Coolify!", fill="#38bdf8", font=font_title_md)
        draw.text((360, 490), "Dukungan Teknis: biztech@proxsisgroup.com • Panel: https://connect.proxsis.com", fill="#f8fafc", font=font_body)
        draw.text((480, 525), "Proxsis IT Infrastructure & Biztech Group • 2026", fill="#94a3b8", font=font_small)
        
        draw_subtitle_card(draw, "SELESAI", "Deployment Selesai & Terstandarisasi • Bebas Edit Reverse Proxy Manual Selamanya!", "Panduan PDF lengkap & video animasi tersimpan di folder proyek Anda.")

    # Convert PIL Image to BGR numpy array and write to FFmpeg stdin
    bgr_frame = np.array(img)[:, :, ::-1]
    proc.stdin.write(bgr_frame.tobytes())
    
    if f % 300 == 0:
        print(f"Rendered frame {f}/{TOTAL_FRAMES} ({sec:.1f}s / {TOTAL_DURATION}s)...")

proc.stdin.close()
proc.wait()
print("Video rendering finished successfully!")
print(f"MP4 output saved at: {mp4_out}")
print(f"File size: {os.path.getsize(mp4_out)} bytes")
