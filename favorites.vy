# pragma version ^0.4.0
# @lisence MIT

my_fav_num: int256
list_of_nums: public(int256[5])
index: uint256

@external
def store(new_number: int256):
    # changing fav number
    self.my_fav_num = new_number

@external
@view
def retrieve() -> int256:
    # to view the number in favorite number same as being public
    return self.my_fav_num

@external
@view
def multiply_by10() -> int256:
    # just multiply it to view with no gas cost
    return self.my_fav_num * 10

@external
def store2list():
    self.list_of_nums[self.index] = self.my_fav_num
    self.index = self.index + 1

# with structure
struct Person:
    favorite_number: uint256
    name: String[100]

list_of_persons: public(Person[5])
persons_index : uint256

@external
def add2person(name:String[100],favorite_number:uint256):
    new_person: Person = Person(favorite_number=favorite_number, name=name)
    self.list_of_persons[self.persons_index] = new_person
    self.persons_index = self.persons_index + 1


@deploy
def __init__():
    # Constractor will run after deploy
    self.my_fav_num = -1
    self.index = 0
    self.persons_index = 0