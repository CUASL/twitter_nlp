ipc = ipcx;
ipc.on;
ipc.publish("test");
while 1
    ipc.send("Hello World from matlab");
    pause(0.5)
end

ipc.off;