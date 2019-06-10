class Solution:
    def numUniqueEmails(self, emails):
        res = []
        for each in emails:
            local, domain = each.split("@")
            tmp = local.split("+")[0].replace(".", "") + "@" + domain
            res.append(tmp)
        return len(set(res))
