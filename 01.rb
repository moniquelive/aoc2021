#!/usr/bin/env ruby

def count_growth(n)
  n.each_cons(2).
    filter { |x,y| x.to_i < y.to_i }.
    size
end

numbers = open('input-01.txt').readlines.map(&:to_i)
print 'part 1: ', count_growth(numbers) # 1766
puts
numbers = numbers.each_cons(3).map { |x,y,z| x.to_i + y.to_i + z.to_i }
print 'part 2: ', count_growth(numbers) # 1797

