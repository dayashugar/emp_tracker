FROM python:3.10.20-alpine3.22
RUN pip3 install matplotlib
RUN mkdir -p /app/data
COPY emp_tracker.py /app/
COPY plotter.py /app/

WORKDIR /app
VOLUME /app
CMD ["python", "emp_tracker.py"]