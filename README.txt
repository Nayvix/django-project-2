Hello!
This is a README for my application cryptids.

In this document I'll report things related to testing and security.

I made 4 main tests, 2 static and 2 dynamic.
The first two (test_Sighting_future and test_Sighting_happened) are related to making sure that Sightings are not taking place in the future,
as the sighting wouldn't have happened yet. It is important to make sure the sightings lists stay clear as scientists would probably investigate areas where
cryptids appeared based of these.
The other two are in the same kind of category, as they make sure that the models show the right information.

For the security part, a config file has been added to make sure the secret key couldn't be found in the app files,
HTTPS has been enabled, and the authentication process now prevents any redirect loop. The files have comments going
into a little bit more detail about how it has been done.

Thank you for reading me.