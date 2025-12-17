# Use official PHP image with Apache
FROM php:8.2-apache

# Install PDO MySQL extension
RUN docker-php-ext-install pdo pdo_mysql

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Create PHP configuration for Apache
RUN echo '<FilesMatch ".+\.php$">\n\
    SetHandler application/x-httpd-php\n\
</FilesMatch>\n\
<FilesMatch ".+\.phps$">\n\
    SetHandler application/x-httpd-php-source\n\
    Require all denied\n\
</FilesMatch>\n\
<FilesMatch "^\.ph(p[3457]?|t|tml)$">\n\
    Require all denied\n\
</FilesMatch>' > /etc/apache2/mods-available/php.conf \
    && a2enmod php

# Set working directory
WORKDIR /var/www/html

# Copy application code
COPY index.php .
COPY .htaccess .

# Update Apache configuration to allow .htaccess
RUN echo '<Directory /var/www/html/>\n\
    Options Indexes FollowSymLinks\n\
    AllowOverride All\n\
    Require all granted\n\
</Directory>' > /etc/apache2/conf-available/docker-php.conf \
    && a2enconf docker-php

# Expose port 80
EXPOSE 80

# Start Apache in foreground
CMD ["apache2-foreground"]
