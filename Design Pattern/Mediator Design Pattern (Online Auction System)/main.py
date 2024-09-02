from .Auction import Auction
from .Bidder import Bidder


auction = Auction()
bidder1 = Bidder("Rahul", auction)
bidder2 = Bidder("Ankit", auction)
bidder3 = Bidder("Anubhav", auction)
bidder4 = Bidder("Gautam", auction)

bidder1.placeBid(1000)
bidder2.placeBid(2000)
bidder3.placeBid(3000)
