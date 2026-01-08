from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


# =========================
# 1. PODACI (ruta)
# =========================

route_data = {
    1533439: {"node":"","level":"Level 1","type":"Standard","product":"WG 350x400 - TROX Technik #88qo9bv#","size":"354/404","length":"","flow":"3400 m³/h","velocity":"","pressure_drop":"63.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1625204: {"node":"","level":"Level 1","type":"Duct","product":"","size":"354/404","length":"360","flow":"3400 m³/h","velocity":"6.6 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1625269: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Transition - Flanged","size":"800/250-354/404","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1555138: {"node":"","level":"Level 1","type":"Duct","product":"","size":"800/250","length":"844","flow":"3400 m³/h","velocity":"4.7 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1625267: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Radius Elbow - Flanged","size":"250/800-250/800","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1555158: {"node":"","level":"Level 1","type":"Duct","product":"","size":"800/250","length":"1615","flow":"3400 m³/h","velocity":"4.7 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1625178: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Transition - Flanged","size":"800/250-800/250","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1555188: {"node":"","level":"Level 1","type":"Duct","product":"","size":"800/250","length":"173","flow":"3400 m³/h","velocity":"4.7 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593620: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Radius Elbow - Flanged","size":"250/800-250/800","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1555157: {"node":"","level":"Level 1","type":"Duct","product":"","size":"800/250","length":"1206","flow":"3400 m³/h","velocity":"4.7 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},

    1625574: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Transition - Flanged","size":"800/250-600/300","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1625569: {"node":"","level":"Level 1","type":"Duct","product":"","size":"600/300","length":"109","flow":"3400 m³/h","velocity":"5.2 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1533433: {"node":"","level":"Level 1","type":"Standard","product":"AHU 01","size":"","length":"","flow":"","velocity":"","pressure_drop":"","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609239: {"node":"","level":"Level 1","type":"Duct","product":"","size":"600/300","length":"500","flow":"3400 m³/h","velocity":"5.2 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609280: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Transition - Flanged","size":"600/300-600/250","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1607308: {"node":"","level":"Level 1","type":"Duct","product":"","size":"600/250","length":"1412","flow":"3400 m³/h","velocity":"6.3 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609278: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Radius Elbow - Flanged","size":"250/600-250/600","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1607322: {"node":"","level":"Level 1","type":"Duct","product":"","size":"600/250","length":"438","flow":"3400 m³/h","velocity":"6.3 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1607368: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Radius Elbow - Flanged","size":"250/600-250/600","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1555114: {"node":"","level":"Level 1","type":"Duct","product":"","size":"600/250","length":"1781","flow":"3400 m³/h","velocity":"6.3 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},

    1607161: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Transition - Flanged","size":"400/400-600/250","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1607092: {"node":"","level":"Level 1","type":"Duct","product":"","size":"400/400","length":"505","flow":"3400 m³/h","velocity":"5.9 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1607099: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Radius Elbow - Flanged","size":"400/400-400/400","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1607066: {"node":"","level":"Level 1","type":"Duct","product":"","size":"400/400","length":"140","flow":"3400 m³/h","velocity":"5.9 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1607082: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Transition - Flanged","size":"500/350-400/400","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1555027: {"node":"","level":"Level 1","type":"Duct","product":"","size":"500/350","length":"989","flow":"3400 m³/h","velocity":"5.4 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593312: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Radius Elbow - Flanged","size":"350/500-350/500","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1554786: {"node":"","level":"Level 1","type":"Duct","product":"","size":"500/350","length":"865","flow":"3400 m³/h","velocity":"5.4 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593342: {"node":"","level":"Level 1","type":"Duct accessory","product":"Rectangular Radius Elbow - Flanged","size":"500/350-500/350","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593333: {"node":"1","level":"Level 1","type":"Duct","product":"","size":"500/350","length":"2955","flow":"3400 m³/h","velocity":"5.4 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593860: {"node":"2","level":"Level 1","type":"Duct accessory","product":"Rectangular Tee Straight - Flanged","size":"500/350-300/350-315/350","length":"","flow":"","velocity":"","pressure_drop":"","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1606741: {"node":"3","level":"Level 1","type":"Duct","product":"","size":"300/350","length":"1500","flow":"1800 m³/h","velocity":"4.8 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},

    1594194: {"node":"","level":"Level 1","type":"Duct accessory","product":"M_Round Takeoff - Shoe","size":"ø315-ø315","length":"","flow":"","velocity":"","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1594404: {"node":"","level":"Level 1","type":"Duct","product":"","size":"ø315","length":"368","flow":"600 m³/h","velocity":"2.1 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609470: {"node":"","level":"Level 1","type":"Duct accessory","product":"Round Transition - Slip Joint","size":"ø315-ø200","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609458: {"node":"","level":"Level 1","type":"Duct","product":"","size":"ø200","length":"699","flow":"600 m³/h","velocity":"5.3 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1594402: {"node":"","level":"Level 1","type":"Duct accessory","product":"CAV controller RN TROX","size":"ø200-ø200","length":"","flow":"","velocity":"","pressure_drop":"150.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609399: {"node":"","level":"Level 1","type":"Duct","product":"","size":"ø200","length":"440","flow":"600 m³/h","velocity":"5.3 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609435: {"node":"","level":"Level 1","type":"Duct accessory","product":"Round Transition - Slip Joint","size":"ø315-ø200","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593000: {"node":"","level":"Level 1","type":"Duct","product":"","size":"ø315","length":"935","flow":"600 m³/h","velocity":"2.1 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593018: {"node":"","level":"Level 1","type":"Duct accessory","product":"Round Elbow Plain - Slip Joint","size":"ø315-ø315","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593023: {"node":"","level":"Level 1","type":"Duct","product":"","size":"ø315","length":"1213","flow":"600 m³/h","velocity":"2.1 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593038: {"node":"","level":"Level 1","type":"Duct accessory","product":"Round Elbow Plain - Slip Joint","size":"ø315-ø315","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1593042: {"node":"","level":"Level 1","type":"Duct","product":"","size":"ø315","length":"785","flow":"600 m³/h","velocity":"2.1 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609491: {"node":"","level":"Level 1","type":"Duct accessory","product":"Round Transition - Slip Joint","size":"ø315-ø250","length":"","flow":"","velocity":"","pressure_drop":"0.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1609488: {"node":"","level":"Level 1","type":"Flex duct","product":"","size":"ø250","length":"1056","flow":"600 m³/h","velocity":"3.4 m/s","pressure_drop":"0","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""},
    1592797: {"node":"","level":"Level 1","type":"Terminal","product":"VDW-Q-Z-H-M TROX Technik","size":"ø250","length":"","flow":"600 m³/h","velocity":"","pressure_drop":"300.0 Pa","k_factor":"0","dp_l":"0","pt":"0","pst":"0","adj":"","warnings":""}
}

def wrap_text_smart(text, max_len=20):
    if not text:
        return ""

    lines = []
    text = text.strip()

    while len(text) > max_len:
        # tražimo poslednji blanko u dozvoljenom opsegu
        split_pos = text.rfind(" ", 0, max_len + 1)

        if split_pos == -1:
            # nema blanko znaka → preseci na max_len
            lines.append(text[:max_len])
            text = text[max_len:]
        else:
            # lomimo po blanko znaku
            lines.append(text[:split_pos])
            text = text[split_pos + 1:]  # preskačemo blanko

    if text:
        lines.append(text)

    return "\n".join(lines)

# =========================
# 2. PRIPREMA TABELE
# =========================

# Nazivi parametara (prvi red)
columns = [
    ("Node", "node"),
    ("Level", "level"),
    ("Type", "type"),
    ("Product", "product"),
    ("Size", "size"),
    ("L [m]", "length"),
    ("Flow [m³/h]", "flow"),
    ("v [m/s]", "velocity"),
    ("dtp [Pa]", "pressure_drop"),
    ("K factor", "k_factor"),
    ("Δp/L", "dp_l"),
    ("pt", "pt"),
    ("pst", "pst"),
    ("adj.", "adj"),
    ("Warnings", "warnings"),
]

table_data = []

# Header
header = [col[0] for col in columns]
table_data.append(header)

for element_id, params in route_data.items():
    row = []
    for col_name, key in columns:
        value = str(params.get(key, ""))

        if key == "product":
            row.append(wrap_text_smart(value, 20))
        else:
            row.append(value[:15])

    table_data.append(row)
# =========================
# 3. KREIRANJE PDF-a
# =========================

pdf_file = "route_report.pdf"
document = SimpleDocTemplate(
    pdf_file,
    pagesize=landscape(A4),
    rightMargin=20,
    leftMargin=20,
    topMargin=20,
    bottomMargin=20
)

table = Table(table_data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),

    # Tekstualne kolone (levo)
    ("ALIGN", (0, 1), (4, -1), "LEFT"),   # Node, Level, Type, Product, Size
    ("ALIGN", (11, 1), (12, -1), "LEFT"), # adj, warnings (pretpos. poslednje dve kolone)

    # Numeričke kolone (desno)
    ("ALIGN", (5, 1), (10, -1), "RIGHT"), # Length, Flow, Velocity, Pressure Drop, k_factor, dp_l, pt, pst

    # Header bold
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
]))


document.build([table])

print("PDF uspešno kreiran:", pdf_file)
