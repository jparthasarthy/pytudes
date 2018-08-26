<div style="text-align:center"><img src ="https://zerogravitylabs.ca/wp-content/uploads/2017/03/WEB_LOGO_WHITE_TEXT.png"/></div>


# ZGL Getting started with Hololens development guide

This guide's purpose is to leave you with a workable knowledge of Unity & Hololens development for projects in the future. This guide includes all of the boilerplate knowledge that was acquired through trial and error so you can get up to speed and start developing quickly. It also includes a walkthrough of some of the most common elements of Unity & Hololens development.

## Getting started

You can't actually build projects for the Hololens on your Mac. You have two options:

1. Develop on your Mac using VS + Unity for Mac, and build it using a Windows machine, like an AWS instance. We didn't try this, but you can follow [this guide](https://www.quora.com/Can-I-setup-a-Microsoft-Hololens-development-environment-on-a-Mac.)

2. Use a Windows disk image and emulate windows on your Mac. You have two options here: Virtualbox (ZGL guide [here](https://www.google.com)) or Bootcamp (Tommy made a guide [here](https://www.google.com). There is noticeable lag using VirtualBox emulation, but Bootcamp takes longer to set up because you have to re-encrpyt your hard-drive.)

To develop with the Hololens, you have two options. You can either use Unity (using c# scripting) or DirectX (mostly C++ but there are C# packages.) Developing in Unity is easier, however, DirectX runs much quicker. This project was Unity-based, so this guide will concern Unity.

### Installing Unity

An important package for developing with the hololens is the Mixed Reality Toolkit. It has many useful utility scripts and allows you to deploy builds directly from Unity to the hololens. **You should use the version of Unity that has a stable relase of MRTK.**. [You can check here.](https://github.com/Microsoft/MixedRealityToolkit-Unity/releases) 

Unity 2017 is in long-term support, and during our project we found no difference between developing in 2017 and developing in 2018. So, our recommendation is to use Unity 2017.4.10. [You can download this here.](https://unity3d.com/get-unity/download/archive) 

### Download options

**The following options are necessary to develop with the hololens:**

- Standard assets                                   
- Windows Store .NET Scripting backend

**Optional packages that may come in handy:**

- Android build support (if you wanted to make your application cross-platform)
- Vuforia AR support (useful for real-world tagging)

In our experience, IL2CPP backend does not play well with the Hololens, so we recommend using .NET scripting backend.

### Installing Visual Studio





