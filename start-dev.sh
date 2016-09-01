#!/bin/bash
# start dev instances for cypriadonato.work: pelican dev server, pelican content generation with auto reload, and compass watching on css

cd ~/git/cypriadonato.work/ && ./develop_server.sh stop && ./develop_server.sh start #stop old instance of dev server and start it again
pelican content -r #launch pelican moulinette, generating the static files, with autoreload or watch
cd output/theme/cypria-donato/static/css/sassaparilla/compass/ && compass watch #start the compass watch on the css
