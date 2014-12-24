import datetime
class TimeFrame(object):
    """ Representation of an ordered set of candles """
    def __init__(self, container=None):
        if container is None:
            container = []
        self.container = container

    def __str__(self):
        return str(self.container)

    def __repr__(self):
        return str(self.container)

    def __getitem__(self, key):
        return TimeFrame(self.container[key])

    def __len__(self):
        return len(self.container)

    def get_average_range(self):
        range_sum = 0
        for unit in self.container:
            range_sum += unit[1].getHL()
        return range_sum/len(self)
    
    def get_monthly_distribution(self):
        """
        Returns volatility(High-Low) distribution by days in list [MO, TU, WE, TH, FR]
        Warning: works only with monthly ticks!
        """
        m_vol = 12*[0]
        m_num = 12*[0]
        m_dist_vol = 12*[0]
        for elem in self.container:
            m_num[elem[0].month] += 1
            m_vol[elem[0].month] += elem[1].getHL()
        for i in range(5):
            if not m_num[i] == 0:
                m_dist_vol[i] = m_vol[i]/m_num[i]
        print(m_vol)
        print(m_num)
        return m_dist_vol        
        
    def get_daily_distribution(self):
        """
        Returns volatility(High-Low) distribution by days in list [MO, TU, WE, TH, FR]
        Warning: works only with daily ticks!
        """
        day_vol = 7*[0]
        day_num = 7*[0]
        day_dist_vol = 7*[0]
        for elem in self.container:
            day_num[elem[0].weekday()] += 1
            day_vol[elem[0].weekday()] += elem[1].getHL()
        for i in range(7):
            if not day_num[i] == 0:
                day_dist_vol[i] = day_vol[i]/day_num[i]
        print(day_vol)
        print(day_num)
        return day_dist_vol

    def get_hourly_distribution(self):
        """
        Returns volatility(High-Low) distribution by days in list [0,1,2,3,...,23]
        Warning: works only with hourly ticks!
        """
        h_vol = 24*[0]
        h_num = 24*[0]
        h_dist_vol = 24*[0]
        for elem in self.container:
            h_num[elem[0].hour] += 1
            h_vol[elem[0].hour] += elem[1].getHL()
        for i in range(24):
            if not h_num[i] == 0:
                h_dist_vol[i] = h_vol[i]/h_num[i]
        return h_dist_vol

