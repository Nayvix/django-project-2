Hello!
This is a README for my application cryptids.

In this document I'll report things related to testing and security.

I made 4 main tests, 2 static and 2 dynamic.
As my app is mainly made to give scientists a database to work on cryptids, the main issues would be that the information is incorrectly displayed because of a bug.
Therefore, the 4 tests I implemented are here to make sure the models and functions display the correct information in the views.

The first two (test_Sighting_future and test_Sighting_happened) are related to making sure that Sightings are not taking place in the future,
as the sighting wouldn't have happened yet. It is important to make sure the sightings lists stay clear as scientists would probably investigate areas where
cryptids appeared based of these.
The other two are in the same kind of category, as they make sure that the models show the right information.

As for the security part, I created a config file to make sure the secret key couldn't be found in the app files, as well as the Root-URLCONF.
The settings.py file will now import configparser to be able to read the config.ini file and retrieve both of these sensible informations,
instead of having them directly written in the python file.

HTTPS has been enabled through setting a lot of HTTPS related flags, as HTTPS is both more secure and trustworthy than HTTP.
The list of allowed hosts has been changed as well, gotten from fully blank to accepting localhost and Nikyar.pythonanywhere.com,
which doesn't work at the moment for an unknown reason I haven't been able to fix (the app doesn't find cryptapps.settings).


Finally, the authentication process now prevents any redirect loop via the permission_required([...]) function. 

The files have comments going into a little bit more detail about how it has been done.
Thank you for reading me.