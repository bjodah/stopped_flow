Laborationshandledning Kemisk dynamik
=====================================

För att generara pdf på Ubuntu:

1. Installera docker om det redan inte är installerat ::

   $ wget -qO- https://get.docker.io/gpg | sudo apt-key add -
   $ sudo sh -c "echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
   $ sudo apt-get update
   $ sudo apt-get install lxc-docker apparmor
   $ sudo docker -d &


2. Generera pdf: ::

   $ ./generate_output.sh


3. Visa resultat: ::

   $ xdg-open out_0/main.pdf; xdg-open out_0/supp_mater.pdf

4. Generera alternativ version (0-3): ::

   $ ./generate_output.sh 1


Senaste versionen finns `här <http://hera.physchem.kth.se/~stopped_flow/>`_.
