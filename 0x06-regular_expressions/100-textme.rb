#!/usr/bin/env ruby
#textme
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
