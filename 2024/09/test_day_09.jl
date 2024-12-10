using Test
include("./day_09.jl")

SIMPLE_INPUT="291"
SIMPLE_INPUT_INITIAL_DISKMAP="00.........1"
SIMPLE_INPUT_FINAL_DISKMAP="001........."
SIMPLE_INPUT_CHECKSUM=2

AOC_INPUT="2333133121414131402"
AOC_INPUT_INITIAL_DISKMAP="00...111...2...333.44.5555.6666.777.888899"
AOC_INPUT_FINAL_DISKMAP="0099811188827773336446555566.............."
AOC_INPUT_CHECKSUM=1928

AOC_INPUT_UNFRAGMENTED_DISKMAP="00992111777.44.333....5555.6666.....8888.."
AOC_INPUT_UNFRAGMENTED_CHECKSUM=2858


function test_solution()

    @testset "Simple Input" begin
        s = Solution(SIMPLE_INPUT)
        @test disk_map_to_string(s)==SIMPLE_INPUT_INITIAL_DISKMAP

        optimize_disk_map(s)
        @test optimized_disk_map_to_string(s)==SIMPLE_INPUT_FINAL_DISKMAP

        @test checksum_disk_map(s)==SIMPLE_INPUT_CHECKSUM
    end

    @testset "AOC Input Part 1" begin
        s = Solution(AOC_INPUT)
        @test disk_map_to_string(s)==AOC_INPUT_INITIAL_DISKMAP

        optimize_disk_map(s)
        @test optimized_disk_map_to_string(s)==AOC_INPUT_FINAL_DISKMAP

        @test checksum_disk_map(s)==AOC_INPUT_CHECKSUM
    end

    @testset "AOC Part 2 Input (Defragmentation)" begin
        s = Solution(AOC_INPUT)

        unfragment_disk_map(s)
        @test unfragmented_disk_map_to_string(s)==AOC_INPUT_UNFRAGMENTED_DISKMAP

        @test unfragmented_checksum_disk_map(s)==AOC_INPUT_UNFRAGMENTED_CHECKSUM
    end
end

test_solution()
