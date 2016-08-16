


def getcomments(r,checkday, username):
        import datetime
        import time
        currentdate = time.strftime("%m/%d/%Y")
        
        currentmonth = time.strftime("%m")
        currentmonth = int(currentmonth)
        currentdaynum = time.strftime("%d")
        currentdaynum = int(currentdaynum)
        currentyear = time.strftime("%Y")
        currentyear = int(currentyear)
        me = r.get_redditor(username)
        print "Finding comments by " + username
        comments = me.get_comments(limit=None)
        
       
        for comment in comments:
                if comment.ups > 100:
                        print "===="
                        ups = comment.ups
                        body = comment.body
                        print ups
                        print body
                        continue
                date = datetime.datetime.fromtimestamp(comment.created_utc)
                if checkday == 1:
                        if date.year != int(currentyear):
                                comment.delete()
                        else:
                                if date.month != int(currentmonth):
                                        comment.delete()
                                else:
                                        if (currentdaynum - 7) > date.day:
                                                comment.delete()
                                        else:
                                                continue
                if checkday == 0:
                        if comment.ups > 100:
                                continue
                        if currentmonth == 1 or currentmonth ==  2 or currentmonth == 4 or currentmonth == 6 or currentmonth == 8 or currentmonth == 9 or currentmonth == 11:
                                PrevMonthDays = 31
                        if currentmonth == 3:
                                PrevMonthDays = 28
                        else:
                                PrevMonthDays == 30
                        
                        var = currentdaynum - 7

                        WeekLimit = var + PrevMonthDays

                        if (int(currentmonth) - 1) != date.month:
                                comment.delete()

                        if date.day > WeekLimit and (Currentmonth - 1) == date.month:
                                comment.delete()
                        
        

def countcomments(r,checkday, username):  
        import datetime
        import time
        currentdate = time.strftime("%m/%d/%Y")
        
        currentmonth = time.strftime("%m")
        currentmonth = int(currentmonth)
        currentdaynum = time.strftime("%d")
        currentdaynum = int(currentdaynum)
        currentyear = time.strftime("%Y")
        currentyear = int(currentyear)
        me = r.get_redditor(username)
        comments = me.get_comments(limit=None)
        
        count = 0
        for comment in comments:
                if comment.ups > 50:
                        count = count + 1
                        continue
                date = datetime.datetime.fromtimestamp(comment.created_utc)
                

                if checkday == 1:
                        if date.year != int(currentyear):
                                count = count + 1
                        else:
                                if date.month != int(currentmonth):
                                        count = count + 1
                                else:
                                        if (currentdaynum - 7) > date.day:
                                                count = count + 1
                                        else:
                                                continue
        return count
def main():
        import praw
        
        import time

        currentdate = time.strftime("%m/%d/%Y")
        currentmonth = time.strftime("%m")
        currentdaynum = time.strftime("%d")
        currentyear = time.strftime("%Y")

        if currentdaynum > 7:
                checkday = 1
        else:
                checkday = 0

        r = praw.Reddit(user_agent='Cleaner)
        username = raw_input("Enter username: ")
        password = raw_input("Enter password: ")
        r.login(username,password,disable_warning=True)
        commentcount = countcomments(r,checkday,username)
        if commentcount > 0:
                getcomments(r,checkday,username)
                main()
        
main()
