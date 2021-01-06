rm -rf $HOME/.cache/google-chrome/Default/Cache/
rm -rf $HOME/.cache/google-chrome/Default/Media\ Cache/
rm -rf $HOME/.cache/google-chrome/Profile\ 2/Cache/
./DB_Browser_for_SQLite--x86_64.AppImage $HOME/.config/google-chrome/Default/Cookies
printf "%s\n" "Cache del chrome limpiado!"
