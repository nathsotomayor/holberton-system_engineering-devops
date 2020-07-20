# Web infrastructure design

Schemas about diferents web infrastructure implementations.

## Schemas:

**0. Simple web stack**

Simple one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. File: [`0-simple_web_stack`](https://github.com/nathsotomayor/holberton-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack)

	* 1 server
	* 1 web server (Nginx)
	* 1 application server
	* 1 application files (code base)
	* 1 database (MySQL)
	* 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

**1. Distributed web infrastructure**

Three server web infrastructure that hosts the website `www.foobar.com`. File: [`1-distributed_web_infrastructure`](https://github.com/nathsotomayor/holberton-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure)

	* 3 servers
	* 1 web server (Nginx)
	* 1 application server
	* 1 load-balancer (HAproxy)
	* 1 application files (code base)
	* 1 database (MySQL)
	
**2. Secured and monitored web infrastructure**

Three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored. File: [`2-secured_and_monitored_web_infrastructure`](https://github.com/nathsotomayor/holberton-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure)

	* 3 servers
	* 1 web server (Nginx)
	* 1 application server
	* 1 load-balancer (HAproxy)
	* 1 application files (code base)
	* 1 database (MySQL)
	* 3 firewalls
	* 1 SSL certificate to serve www.foobar.com over HTTPS
	* 3 monitoring clients (data collector for Sumologic or other monitoring services)
	

## Author

Made with  by Nathaly Sotomayor Ampudia

[LinkedIn](https://www.linkedin.com/in/nathsotomayor/) · [Twitter](https://twitter.com/nathsotomayor) · [GitHub profile](https://github.com/nathsotomayor)
