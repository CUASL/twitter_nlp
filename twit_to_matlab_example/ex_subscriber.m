addpath('ipcx')
ipc = ipcx;
ipc.on;
ipc.subscribe2('test',@fx)