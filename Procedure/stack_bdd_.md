
```
# Use root login
version: '2'

services:
  db:
    image: mysql
    container_name: mysql
    # NOTE: use of "mysql_native_password" is not recommended:
    # https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password
    # (this is just an example, not intended to be a production configuration)
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    ports:
      - 3306:3306
    volumes:
      - mysql-volume:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: votre_mdp root

  adminer:
    image: adminer
    container_name: adminer
    restart: always
    ports:
      - 8080:8080
      
volumes:
  mysql-volume:


```
