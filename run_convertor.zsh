# chmod +x run_convertor.zsh
# alias run_main='/path/to/run_convertor.zsh'

cd /path/to/directory/conv
python3 main.py
osascript -e 'tell application "Terminal" to quit'
