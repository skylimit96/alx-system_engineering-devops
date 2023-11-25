#!/usr/bin/pup

# Install a specific version of Flask (2.1.0)
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'], # Ensure that pip is installed first
}
