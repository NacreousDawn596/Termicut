echo 'setting file'
mkdir ~/.local/share/NacreousDawn596/
mkdir ~/.local/share/NacreousDawn596/Termicut/
cd ..
mv Termicut/* ~/.local/share/NacreousDawn596/Termicut/
sleep 1
clear
echo 'configuring settings'
sleep 1
echo '' >> ~/.bashrc
touch ~/.local/share/NacreousDawn596/termicut/.shortcut.sh
echo 'source ~/.local/share/NacreousDawn596/termicut/.shortcut.sh' >> ~/.bashrc
echo '' >> ~/.bashrc
rm ~/.local/share/NacreousDawn596/termicut/setup.sh
clear
echo 'done!'
echo 'now you can launche it after closing the terminals by writing short'
