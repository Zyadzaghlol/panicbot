PANIC_DB = {

# WATCHDOG / SENSORS
"TP1A": {"cat":"Battery","issue":"Battery thermal sensor","fix":["Replace battery","Check connector"],"p":"High"},
"TP2": {"cat":"Battery/Display","issue":"Thermal sensor","fix":["Check battery + screen"],"p":"Medium"},
"TP3R": {"cat":"CPU/Display","issue":"CPU line issue","fix":["Reball CPU","Check screen"],"p":"Critical"},
"TP4H": {"cat":"Battery","issue":"Thermal sensor","fix":["Check battery"],"p":"Medium"},
"TGOB": {"cat":"Battery","issue":"Battery communication","fix":["Check gas gauge","Replace battery"],"p":"High"},
"TGOV": {"cat":"Charging","issue":"Charging temp sensor","fix":["Replace charging flex"],"p":"Medium"},
"TTSA": {"cat":"Charging","issue":"Dock temp sensor","fix":["Check dock"],"p":"Medium"},
"PRSO": {"cat":"Charging","issue":"Pressure sensor","fix":["Check dock flex"],"p":"Medium"},

# MICROPHONES
"MIC1": {"cat":"Audio","issue":"Bottom mic","fix":["Replace charging flex"],"p":"Medium"},
"MIC2": {"cat":"Audio","issue":"Rear mic","fix":["Check rear mic"],"p":"Medium"},
"MIC3": {"cat":"Audio","issue":"Front mic","fix":["Check earpiece flex"],"p":"Medium"},
"MIC4": {"cat":"Audio","issue":"Right mic","fix":["Check dock flex"],"p":"Medium"},

# NAND / STORAGE
"600SECONDS": {"cat":"NAND","issue":"NAND timeout","fix":["Reball NAND","Replace NAND"],"p":"Critical"},
"310SECONDS": {"cat":"Board","issue":"Mainboard timeout","fix":["Reball CPU/NAND"],"p":"Critical"},
"NVME": {"cat":"Storage","issue":"NVMe failure","fix":["Replace NAND"],"p":"Critical"},
"ANS": {"cat":"Storage","issue":"NAND controller","fix":["Check PCB lines"],"p":"Critical"},
"EMEMORY": {"cat":"Storage","issue":"Memory error","fix":["Replace NAND"],"p":"Critical"},
"LINK TIMEOUT": {"cat":"Storage","issue":"NAND link issue","fix":["Check CPU-NAND"],"p":"Critical"},

# CPU
"SOC HOT": {"cat":"CPU","issue":"Overheating","fix":["Reball CPU","Check short"],"p":"Critical"},
"COHERENCY ERROR": {"cat":"CPU","issue":"CPU internal error","fix":["Reball CPU"],"p":"Critical"},
"TH0": {"cat":"CPU","issue":"Thermal issue","fix":["Check CPU heat"],"p":"High"},
"CPU HALT": {"cat":"CPU","issue":"CPU not responding","fix":["Reball CPU"],"p":"Critical"},
"PARITY ERROR": {"cat":"CPU","issue":"Memory parity error","fix":["Check SDRAM/NAND"],"p":"Critical"},

# BASEBAND
"BASEBAND": {"cat":"Network","issue":"No signal","fix":["Repair baseband"],"p":"Critical"},
"RADIO FAILED": {"cat":"Network","issue":"RF issue","fix":["Check RF IC"],"p":"High"},
"PCIE BASEBAND": {"cat":"Network","issue":"PCIe baseband error","fix":["Reball baseband"],"p":"Critical"},

# WIFI
"BCMWLAN": {"cat":"WiFi","issue":"WiFi IC","fix":["Replace WiFi IC"],"p":"High"},
"APCIE(WLAN)": {"cat":"WiFi","issue":"WiFi module","fix":["Check module"],"p":"High"},
"L2C": {"cat":"WiFi","issue":"Cache error","fix":["Check WiFi/audio"],"p":"Medium"},

# CHARGING
"TRISTAR2": {"cat":"Charging","issue":"Charging IC","fix":["Replace Tristar"],"p":"High"},
"HYDRA": {"cat":"Charging","issue":"USB IC","fix":["Replace Hydra"],"p":"High"},
"PPM": {"cat":"Power","issue":"Power path IC","fix":["Check PMIC"],"p":"High"},

# DISPLAY
"IOMFB": {"cat":"Display","issue":"Framebuffer","fix":["Replace screen"],"p":"Medium"},
"DCP PANIC": {"cat":"Display","issue":"Display CPU","fix":["Check display power"],"p":"High"},
"DISPLAY PMU": {"cat":"Display","issue":"Display power IC","fix":["Check IC"],"p":"High"},

# CAMERA
"DART-ISP": {"cat":"Camera","issue":"Camera power","fix":["Check camera"],"p":"Medium"},
"AMCC ERROR": {"cat":"Camera","issue":"Front cam","fix":["Replace front cam"],"p":"Medium"},
"ISP ERROR": {"cat":"Camera","issue":"Camera ISP","fix":["Check lines"],"p":"Medium"},

# AOP
"AOP PANIC": {"cat":"Sensors","issue":"Sensor failure","fix":["Check proximity"],"p":"High"},
"SYSTICKWATCHDOG": {"cat":"Audio","issue":"Speaker issue","fix":["Check speaker"],"p":"Medium"},
"GYRO": {"cat":"Sensor","issue":"Gyroscope","fix":["Replace gyro"],"p":"Medium"},

# I2C
"I2C0": {"cat":"I2C","issue":"Bus error","fix":["Check charging port"],"p":"Medium"},
"I2C1": {"cat":"I2C","issue":"Bus error","fix":["Check flex"],"p":"Medium"},
"I2C2": {"cat":"I2C","issue":"Peripheral error","fix":["Check camera/display"],"p":"Medium"},

# POWER
"WDT TIMEOUT": {"cat":"Power","issue":"Watchdog timeout","fix":["Check battery"],"p":"High"},
"SMC PANIC": {"cat":"Power","issue":"Power IC","fix":["Check PMIC"],"p":"High"},
"KERNEL ABORT": {"cat":"Power","issue":"Kernel crash","fix":["Check CPU"],"p":"High"},

# SEP
"SEP ROM": {"cat":"Security","issue":"CPU link","fix":["Reball CPU"],"p":"Critical"},
"SEP MEMORY": {"cat":"Security","issue":"SEP fail","fix":["Board repair"],"p":"Critical"},
"SEP I2C": {"cat":"Security","issue":"I2C issue","fix":["Check antenna"],"p":"High"},

# GPU
"GPU": {"cat":"GPU","issue":"GPU failure","fix":["Reball GPU"],"p":"High"},
"AGX": {"cat":"GPU","issue":"Accelerator error","fix":["Check GPU"],"p":"High"},

# OTHER
"BUS ERROR": {"cat":"Board","issue":"PCB issue","fix":["Check layers"],"p":"Critical"},
"TIMEOUT": {"cat":"General","issue":"System timeout","fix":["Check multiple"],"p":"Medium"},
"ASSERTION FAILED": {"cat":"Firmware","issue":"Firmware issue","fix":["Restore iOS"],"p":"Low"},
}