from leet_code.hash_table.minimum_index_sum import Solution


def test_main_1():
    s = Solution()
    assert ["Shogun"] == s.find_restaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                           ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse",
                                            "Shogun"])
