#!/usr/bin/env ruby

lines = open('input-02.txt').readlines.map(&:split)

aim = h_pos = depth_part1 = depth_part2 = 0
lines.each do |(direction, amt)|
  if direction == 'forward'
    h_pos += amt.to_i
    depth_part2 += amt.to_i * aim
  elsif direction == 'down'
    depth_part1 += amt.to_i
    aim += amt.to_i
  elsif direction == 'up'
    depth_part1 -= amt.to_i
    aim -= amt.to_i
  end
end

puts "part 1: #{ h_pos * depth_part1 }"
puts "part 2: #{ h_pos * depth_part2 }"
