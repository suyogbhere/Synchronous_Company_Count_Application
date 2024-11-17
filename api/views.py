from rest_framework import viewsets
from app.models import Company_data, File
from api.serializers import CompanyDataSerializer,FileSerializer
from rest_framework import status
from rest_framework.response import Response
import csv


class CompanyDataViewset(viewsets.ModelViewSet):
    queryset = Company_data.objects.all()     # Define the data to expose
    serializer_class = CompanyDataSerializer     # Link the serializer


class FileViewset(viewsets.ModelViewSet):
    queryset = File.objects.all()     # Define the data to expose
    serializer_class = FileSerializer     # Link the serializer

    def create(self, request, *args, **kwargs):
        # Check if a file is provided
        csv_file = request.FILES.get('file')
        print('CSV_FILE',csv_file)
        if not csv_file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            print('DECODED_FILE',decoded_file)
            reader = csv.DictReader(decoded_file)
            print('READER',reader)

            data_list = []
            print('DATA_LIST:',data_list)
            errors = []
            print('ERROR_LIST:',errors)
            invalid_rows = []  # List to store rows with errors
            print("invalid_rows:",invalid_rows)
            valid_data = []  # List to store valid rows
            print("valid_data:",valid_data)
            try:
                for row in reader:
                    serializer = FileSerializer(data=row)
                    if serializer.is_valid():
                        valid_data.append(File(**serializer.validated_data))
                    else:
                        invalid_rows.append({'row': row, 'errors': serializer.errors})

                # Save all valid data   
                if valid_data:
                    File.objects.bulk_create(valid_data)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Always return a response
            return Response({
                'message': 'File processed.',
                'success_count': len(valid_data),
                'failed_count': len(invalid_rows),
                'invalid_rows': invalid_rows
            }, status=status.HTTP_207_MULTI_STATUS)
            # for row in reader:
            #     serializer = self.get_serializer(data=row)
            #     print('SERIALIZER:',serializer)
            #     if not serializer.is_valid():
            #         print("Invalid Row:", row)
            #         print("Errors:", serializer.errors)
            #         return Response({
            #             'error': 'Validation failed for one or more rows.',
            #             'invalid_row': row,
            #             'validation_errors': serializer.errors},
            #               status=status.HTTP_400_BAD_REQUEST)
            #         errors.append({'row': row, 'errors': serializer.errors})
            #         data_list.append(serializer.validated_data)
            #     else:
            #         return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            # # Bulk create for performance
            # File.objects.bulk_create([File(**data) for data in data_list])
            # return Response({'success': f'{len(data_list)} records uploaded'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)