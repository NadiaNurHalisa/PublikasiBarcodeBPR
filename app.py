from datetime import datetime
import pytz
import streamlit as st

st.set_page_config(
    page_title="Verifikasi Dokumen - BPR Bank Daerah Pati",
    page_icon="🏦",
    layout="centered",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
    a[href*="share.streamlit.io/user"] {display: none !important;}
    img[alt="App Creator Avatar"] {display: none !important;}
    :root { --navy: #082b61; --blue: #1261b0; --cyan: #28b8d7; --ink: #13243b; --muted: #62738b; --line: #d8e5f2; }
    .stApp { min-height: 100vh; background: radial-gradient(circle at 8% 4%, rgba(40,184,215,.20), transparent 28%), radial-gradient(circle at 95% 18%, rgba(18,97,176,.18), transparent 30%), linear-gradient(145deg, #eef7ff 0%, #f7fbff 53%, #e8f1fb 100%); color: var(--ink); font-family: 'DM Sans', sans-serif; }
    .stApp > header, [data-testid='stHeader'] { background: transparent; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid='stToolbar'] { visibility: hidden; }
    .block-container { max-width: 700px; padding: 42px 22px 48px; }
    .app-frame { background: rgba(255,255,255,.94); border: 1px solid rgba(144,181,216,.45); border-radius: 28px; box-shadow: 0 24px 60px rgba(8,43,97,.15), 0 4px 12px rgba(8,43,97,.05); box-sizing: border-box; margin: 0 auto; min-height: 500px; overflow: hidden; padding: 30px 38px 31px; position: relative; width: 500px; }
    .verified-panel { background: linear-gradient(115deg, #eaf7ff, #f2fbff); border: 1px solid #9ed9ed; border-radius: 16px; color: var(--navy); font-size: 17px; font-weight: 800; margin-bottom: 20px; padding: 16px; text-align: center; }
    .header-subtitle { color: var(--blue); font-size: 12px; font-weight: 800; letter-spacing: .16em; text-align: center; }
    .header-title { color: var(--navy); font-family: 'Plus Jakarta Sans', sans-serif; font-size: clamp(21px,4vw,29px); font-weight: 800; line-height: 1.28; margin: 9px 0 22px; text-align: center; }
    .rule { border: 0; border-top: 1px solid var(--line); margin: 0 0 21px; }
    .badge-status { background: #e8f5ff; border: 1px solid #b6d9f2; border-radius: 999px; color: var(--blue); display: inline-block; font-size: 12px; font-weight: 800; margin-bottom: 13px; padding: 7px 12px; }
    .intro { font-size: 16px; margin: 0 0 12px; }
    .card-inside { background: linear-gradient(145deg, #f9fcff, #f1f8ff); border: 1px solid var(--line); border-radius: 17px; box-shadow: 0 8px 22px rgba(18,97,176,.07); padding: 19px 20px 14px; }
    .signer { align-items: center; color: var(--navy); display: flex; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 800; gap: 10px; margin: 0 0 13px; }
    .avatar { align-items: center; background: linear-gradient(145deg, #d8f4ff, #c9dcff); border-radius: 50%; display: inline-flex; font-size: 20px; height: 39px; justify-content: center; width: 39px; }
    .card-rule { border: 0; border-top: 1px solid var(--line); margin: 0 0 13px; }
    .detail-row { display: grid; grid-template-columns: 145px 15px 1fr; line-height: 1.45; margin: 7px 0; }
    .detail-label { color: var(--muted); }
    .detail-value { font-weight: 700; }
    .time-box { background: #e8f4ff; border: 1px solid #c9e2f5; border-radius: 12px; color: #42627f; font-size: 14px; margin-top: 17px; padding: 11px 14px; text-align: center; }
    .footer { color: #6d829a; font-size: 13px; margin-top: 18px; text-align: center; }
    @media (max-width: 600px) { .block-container { padding: 18px 13px 30px; } .app-frame { border-radius: 21px; padding: 25px 18px 23px; } .detail-row { grid-template-columns: 112px 14px 1fr; } .signer { font-size: 17px; } }
    </style>
    """,
    unsafe_allow_html=True,
)

hari_list = {
    "Monday": "Senin",
    "Tuesday": "Selasa",
    "Wednesday": "Rabu",
    "Thursday": "Kamis",
    "Friday": "Jumat",
    "Saturday": "Sabtu",
    "Sunday": "Minggu",
}

bulan_list = {
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember",
}

# Pengaturan zona waktu ke Waktu Indonesia Barat (WIB)
tz_wib = pytz.timezone("Asia/Jakarta")
now = datetime.now(pytz.utc).astimezone(tz_wib)

tanggal_tanda_tangan = f"{hari_list[now.strftime('%A')]}, {now.day} {bulan_list[now.month]} {now.year} pukul {now.strftime('%H:%M')} WIB"

# Menggunakan st.query_params yang kompatibel dengan versi Streamlit terbaru
halaman = st.query_params.get("halaman", "awal")

st.markdown(
    "<div class='header-subtitle'>NASKAH DINAS INI DIKELOLA OLEH</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='header-title'>PT BANK PEREKONOMIAN RAKYAT<br>BANK DAERAH PATI</div>",
    unsafe_allow_html=True,
)
st.markdown("<hr class='rule'>", unsafe_allow_html=True)

if halaman == "disahkan":
    st.markdown(
        "<div class='verified-panel'>✔ NASKAH INI TELAH DISAHKAN DAN TERVERIFIKASI</div>",
        unsafe_allow_html=True,
    )

st.markdown(
    "<span class='badge-status'>✔ RESMI &amp; TERVERIFIKASI</span>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='intro'><b>Naskah ini telah ditandatangani secara sah oleh :</b></p>",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class='card-inside'>
        <div class='signer'><span class='avatar'>👤</span>Dr. Arif Budiarto, SE., MM</div>
        <hr class='card-rule'>
        <div class='detail-row'><span class='detail-label'>Jabatan</span><span>:</span><span class='detail-value'>Direktur Utama</span></div>
        <div class='detail-row'><span class='detail-label'>Unit</span><span>:</span><span class='detail-value'>PT. BPR BANK DAERAH PATI</span></div>
        <div class='detail-row'><span class='detail-label'>Instansi</span><span>:</span><span class='detail-value'>Badan Usaha Milik Daerah</span></div>
        <div class='time-box'>🕘 Ditandatangani pada: <b>{tanggal_tanda_tangan}</b></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='footer'>© 2026 PT BPR Bank Daerah Pati</div>",
    unsafe_allow_html=True,
)
