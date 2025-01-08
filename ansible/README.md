# Ansible Server Configuration

Project URL: https://roadmap.sh/projects/configuration-management

This project contains Ansible playbooks for configuring a Linux server with basic security, Nginx web server, and application deployment capabilities.

## Project Structure
```
.
├── inventory.ini
├── setup.yml
└── roles/
    ├── base/
    │   ├── tasks/
    │   ├── handlers/
    │   └── templates/
    ├── nginx/
    │   ├── tasks/
    │   ├── handlers/
    │   └── templates/
    ├── app/
    │   └── tasks/
    └── ssh/
        ├── tasks/
        ├── handlers/
        └── templates/
```

## Requirements

1. Local machine:
   - Ansible installed
   - SSH key pair generated

2. Remote server:
   - Ubuntu/Debian Linux server
   - Root access or sudo privileges
   - SSH access configured

## Role Descriptions

1. **base**
   - System updates
   - Essential packages installation
   - fail2ban configuration
   - UFW firewall setup

2. **nginx**
   - Nginx installation and configuration
   - UFW rules for HTTP/HTTPS
   - Virtual host setup

3. **app**
   - Application directory creation
   - Website deployment
   - Git repository deployment (stretch goal)

4. **ssh**
   - SSH key management
   - SSH security configuration

## Usage

1. Configure inventory:
```ini
# inventory.ini
[webservers]
webserver ansible_host=YOUR_SERVER_IP ansible_user=root ansible_ssh_private_key_file=~/.ssh/id_rsa
```

2. Run all roles:
```bash
ansible-playbook setup.yml
```

3. Run specific roles using tags:
```bash
# Run only nginx configuration
ansible-playbook setup.yml --tags "nginx"

# Run base and ssh configuration
ansible-playbook setup.yml --tags "base,ssh"
```

## Variables

You can customize the configuration by modifying these variables:

```yaml
# In setup.yml or group_vars
nginx_port: 80
app_directory: /var/www/html
website_tarball: "http://example.com/website.tar.gz"  # Optional
repo_url: "https://github.com/trxngxx/ROADMAP-SH.git"      # Optional for stretch goal
ssh_public_key: "ssh-rsa AAAA..."                    # Your SSH public key
```

## Security Features

1. **System Security**
   - Regular updates
   - fail2ban for brute force protection
   - UFW firewall configuration

2. **SSH Security**
   - Key-based authentication only
   - Root login disabled
   - SSH hardening configurations

3. **Web Security**
   - Nginx security best practices
   - Default server configuration

## Stretch Goal Implementation

To deploy from a GitHub repository instead of a tarball:

1. Update the variables:
```yaml
repo_url: "https://github.com/trxngxx/ROADMAP-SH.git"
```

2. Run the playbook with app tag:
```bash
ansible-playbook setup.yml --tags "app"
```

## Troubleshooting

1. **SSH Connection Issues**
   - Verify SSH key permissions (should be 600)
   - Check server IP and SSH port
   - Ensure proper user permissions

2. **Nginx Issues**
   - Check logs: `/var/log/nginx/error.log`
   - Verify port availability
   - Check UFW rules

3. **Application Deployment**
   - Verify directory permissions
   - Check Git repository access
   - Validate tarball URL

## Best Practices

1. **Security**
   - Regularly update SSH keys
   - Monitor fail2ban logs
   - Keep system packages updated

2. **Maintenance**
   - Regularly test playbooks
   - Keep inventory updated
   - Document custom configurations

3. **Development**
   - Test changes in staging environment
   - Use version control for playbooks
   - Follow Ansible best practices

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.