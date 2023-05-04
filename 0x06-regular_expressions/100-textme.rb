#!/usr/bin/env ruby
puts ARGV[0].scan(/(From:(.+)|To:(.+)|Flags:(.+))/).join
