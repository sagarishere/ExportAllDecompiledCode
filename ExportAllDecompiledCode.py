# Jython script to export all functions' pseudo-code
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

program = getCurrentProgram()
ifc = DecompInterface()
ifc.openProgram(program)

output_file = askFile("Choose Output File", "Save")
with open(output_file.absolutePath, 'w') as f:
    fm = currentProgram.getFunctionManager()
    functions = list(program.getFunctionManager().getFunctions(True))
    monitor = ConsoleTaskMonitor()

    for function in functions:
        res = ifc.decompileFunction(function, 60, monitor)
        if res and res.decompileCompleted():
            code = res.getDecompiledFunction().getC()
            f_name = function.getName()
            f_addr = function.getEntryPoint()
            f_header = "\n// Function: {} @ {}\n".format(f_name, f_addr)
            f_content = "{}\n\n".format(code)
            f.write(f_header + f_content)

print("Decompilation complete: {}".format(output_file.absolutePath))
