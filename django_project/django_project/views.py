from django.shortcuts import render
from ElectricityBills.models import MeterRequest,PayBills,Payment
from WaterBills.models import WaterMeter,WaterMeterReading,CollectingWaterBills
from GasBills.models import ProvideGasMeter,NaturalGasReading,CollectingGasBills
from Buildings.models import BuildingPermitApplications,CollectingReconciliationBuilding

def services(request):
    return render(request, 'services.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
#all dashboard funcitons here 
def dashboard(request):
    return render(request,'Dashboard/project.html')

def electricityServices(request):
    return render(request,'Dashboard/electric.html')

def dashelec1(request):
    meter_requests = MeterRequest.objects.all()
    context = {'meter_requests': meter_requests}
    return render(request, 'Dashboard/dashelec1.html', context)

def dashelec2(request):
        pay_bills = PayBills.objects.all()
        context = {'pay_bills': pay_bills}
        return render(request,'Dashboard/dashelec2.html',context)

def dashelec3(request):
        payment = Payment.objects.all()
        context = {'payment': payment}
        return render(request,'Dashboard/dashelec3.html',context)

def waterSerivces(request):
     return render(request,'Dashboard/water.html')

def dashwater1(request):
    water_meter = WaterMeter.objects.all()
    context = {'water_meter': water_meter}
    return render(request, 'Dashboard/dashwater1.html', context)

def dashwater2(request):
        pay_bills = WaterMeterReading.objects.all()
        context = {'pay_bills': pay_bills}
        return render(request,'Dashboard/dashwater2.html',context)

def dashwater3(request):
        collect_water_bills = CollectingWaterBills.objects.all()
        context = {'collect_water_bills': collect_water_bills}
        return render(request,'Dashboard/dashwater3.html',context)

def gasSerivces(request):
     return render(request,'Dashboard/gaz.html')

def dashgas1(request):
    provide_gas_meter = ProvideGasMeter.objects.all()
    context = {'provide_gas_meter': provide_gas_meter}
    return render(request, 'Dashboard/dashgaz1.html', context)

def dashgas2(request):
        natural_gas_reading = NaturalGasReading.objects.all()
        context = {'natural_gas_reading': natural_gas_reading}
        return render(request,'Dashboard/dashgaz2.html',context)

def dashgas3(request):
        collecting_gas_bills = CollectingGasBills.objects.all()
        context = {'collecting_gas_bills': collecting_gas_bills}
        return render(request,'Dashboard/dashgaz3.html',context)

def buildingSerivces(request):
     return render(request,'Dashboard/building.html')

def dashbuild1(request):
    building_applications = BuildingPermitApplications.objects.all()
    context = {'building_applications': building_applications}
    return render(request, 'Dashboard/dashbuild1.html', context)

def dashbuild2(request):
        collecting_building = CollectingReconciliationBuilding.objects.all()
        context = {'collecting_building': collecting_building}
        return render(request,'Dashboard/dashbuild2.html',context)

