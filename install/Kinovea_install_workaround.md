1. Launch Powershell elevated
2. dotnetfx_wu.reg
3. Reboot

4. Launch Powershell elevated:
```
    DISM /Online /Add-Capability /CapabilityName:NetFx3~~~~
```

5. restore_dotnetfx_wu.reg
6. Reboot

7. https://www.kinovea.org/download.html


References:
Kinovea for Dummies:
http://faculty.sites.uci.edu/loudonlab/files/2016/08/Kinovea-for-Dummies.pdf

Dot Net FX install error on Windows 10: https://www.winhelponline.com/blog/error-0x800f0954-net-framework-3-5-optional-feature-dism/