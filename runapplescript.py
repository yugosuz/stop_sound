import serial
import atexit
import subprocess
import sys

ser = serial.Serial("シリアルポート名", 115200)

def all_done():
    # 終了時の処理
    print("\nDone!")
    ser.close()

def main():
    atexit.register(all_done)
    try:
        while(True):
            line = ser.readline().strip().decode('utf-8')
            # 何かしらのトリガーがあったらスクリプトを実行する。
            # 今回はシリアルモニタから"detected"という文字列が送られてきたら実行する。
            if line == "detected":
                subprocess.run(["osascript", "/path/to/stopyoutube.scpt"])
                print("stopped!")

    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
