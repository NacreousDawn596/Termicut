echo 'setting file'
mkdir ~/.local/share/NacreousDawn596/
cd ..
mv Termicut/ ~/.local/share/NacreousDawn596/
sleep 1
clear
echo 'configuring settings'
sleep 1
echo '' >> ~/.bashrc
touch ~/.local/share/NacreousDawn596/Termicut/.shortcut.sh
echo 'source ~/.local/share/NacreousDawn596/Termicut/.shortcut.sh' >> ~/.bashrc
echo '' >> ~/.bashrc
rm ~/.local/share/NacreousDawn596/Termicut/setup.sh
clear
echo 'done!'
echo 'now you can launch it after reopening the terminal and writing short'
