#!/usr/bin/env ruby

lines = open('input-05.txt').
  readlines.
  map(&:chomp).
  map { |l| l.split(' -> ').map { _1.split(',').map(&:to_i) } }

m1 = Hash.new(0)
m2 = Hash.new(0)
lines.each do |((x1,y1),(x2,y2))|
    if x1 == x2 # vertical
        ([y1, y2].min .. [y1, y2].max).each do |y|
            m1[[x1, y]] += 1
            m2[[x1, y]] += 1
        end
    elsif y1 == y2 # horizontal
        ([x1, x2].min .. [x1, x2].max).each do |x|
            m1[[x, y1]] += 1
            m2[[x, y1]] += 1
        end
    else # diagonal
        dx = x1 > x2 ? -1 : +1
        dy = y1 > y2 ? -1 : +1
        x, y = x1, y1
        while (x != x2) && (y != y2)
            m2[[x, y]] += 1
            x += dx
            y += dy
        end
        m2[[x, y]] += 1
    end
end

print("part 1: ", m1.values.filter { _1 > 1 }.size, "\n")
print("part 2: ", m2.values.filter { _1 > 1 }.size, "\n")
