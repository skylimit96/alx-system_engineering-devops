#!/usr/bin/env ruby
#phone_number
puts ARGV[0].scan(/^\d{10,10}$/).join
