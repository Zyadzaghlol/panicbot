PANIC_DB = {

# WATCHDOG
"TP1A": {"issue": "Battery thermal sensor", "fix": "Replace battery or check connector"},
"TGOB": {"issue": "Battery communication error", "fix": "Check battery IC / connector"},
"MIC1": {"issue": "Bottom mic", "fix": "Check charging flex"},
"MIC2": {"issue": "Rear mic", "fix": "Check rear mic"},
"600SECONDS": {"issue": "NAND failure", "fix": "Reball or replace NAND"},
"310SECONDS": {"issue": "Board issue", "fix": "Check CPU/NAND reball"},
"BACKBOARD": {"issue": "Tristar IC", "fix": "Replace U2 IC"},

# AOP
"AOP PANIC": {"issue": "Sensor failure", "fix": "Check front cam / proximity"},
"SYSTICKWATCHDOG": {"issue": "Audio issue", "fix": "Check speaker/audio IC"},
"AMCC ERROR": {"issue": "Front cam", "fix": "Check front camera"},
"PRESSURECONTROLLER": {"issue": "Proximity", "fix": "Check sensor flex"},

# HARDWARE
"SOC HOT": {"issue": "CPU overheating", "fix": "Reball CPU"},
"BCMWLAN": {"issue": "WiFi IC", "fix": "Replace WiFi IC"},
"TRISTAR2": {"issue": "Charging IC", "fix": "Replace Tristar"},

# DCP
"IOMFB": {"issue": "Display error", "fix": "Check screen"},
"DCP PANIC": {"issue": "Display CPU", "fix": "Check display power"},

# DART
"DART-USB": {"issue": "USB issue", "fix": "Check charging port"},
"DART-ISP": {"issue": "Camera issue", "fix": "Check camera"},

# SEP
"SEP ROM": {"issue": "CPU connection", "fix": "Reball CPU"},
"SEP MEMORY": {"issue": "SEP memory", "fix": "Board repair"},

# SMC
"SMC PANIC": {"issue": "Power issue", "fix": "Check power IC"},

# BASEBAND
"BASEBAND": {"issue": "No signal", "fix": "Repair baseband"},

# NAND
"NVME": {"issue": "Storage failure", "fix": "Replace NAND"},
"ANS": {"issue": "NAND controller", "fix": "Check PCB"},

# CPU
"COHERENCY ERROR": {"issue": "CPU error", "fix": "Reball CPU"},
"TH0": {"issue": "Thermal issue", "fix": "Check CPU heat"},

# POWER
"WDT TIMEOUT": {"issue": "Power issue", "fix": "Check battery"},

# WIFI
"APCIE(WLAN)": {"issue": "WiFi module", "fix": "Check WiFi IC"},

# I2C
"I2C0": {"issue": "Bus error", "fix": "Check charging port"},
"I2C1": {"issue": "Bus error", "fix": "Check flex"},
}