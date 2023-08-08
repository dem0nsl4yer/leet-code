class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        maA, daA = int(arriveAlice[:2]), int(arriveAlice[3:])
        mlA, dlA = int(leaveAlice[:2]), int(leaveAlice[3:])
        maM, daM = int(arriveBob[:2]), int(arriveBob[3:])
        mlM, dlM = int(leaveBob[:2]), int(leaveBob[3:])
        dl = da = 0 
        # choose the later max - arrival and first - min departure  
        #print(daA)
        if maM == maA:
            da = max(daA, daM)
        #print(da)
        if mlA == mlM:
            dl = min(dlA, dlM)  
        #print(dl)
        return (dl - da+1)    