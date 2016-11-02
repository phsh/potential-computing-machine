FROM python
RUN mkdir /dates
COPY dates.py ./dates
CMD ["./dates/dates.py"]