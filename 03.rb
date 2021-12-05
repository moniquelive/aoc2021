#!/usr/bin/env ruby

lines = open('input-03.txt').readlines.map(&:chomp).map(&:chars).map { _1.map(&:to_i) }

epsilon = lines[0].length.times.map do |col|
    ncol = lines.map { _1[col] }
    ncol.count(1) >= (lines.length / 2) ? 1 : 0
end
gamma = epsilon.map { 1 - _1 }

puts "part1: #{epsilon.join.to_i(2) * gamma.join.to_i(2)}"

oxygen = lines.dup
col = 0
while oxygen.length > 1
    ones = oxygen.map { _1[col] }.count(1)
    zeros = oxygen.length - ones
    delta = ones - zeros
    keep = delta > 0 ? 1 : delta < 0 ? 0 : 1
    oxygen.delete_if { _1[col] == keep }
    col += 1
end

co2 = lines.dup
col = 0
while co2.length > 1
    ones = co2.map { _1[col] }.count(1)
    zeros = co2.length - ones
    delta = ones - zeros
    keep = delta > 0 ? 0 : delta < 0 ? 1 : 0
    co2.delete_if { _1[col] == keep }
    col += 1
end

puts "part2: #{oxygen.first.join.to_i(2) * co2.first.join.to_i(2)}"

